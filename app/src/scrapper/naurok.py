import asyncio
import aiohttp

from urllib.parse import urlparse

from src.config import COOKIES, HEADERS

from src.utils.alias import bs4lxml
from src.utils.alias import SUBJECT_LITERAL, KLAS_LITERAL

from src.models.test_info import BaseTestInfo, TestInfo, Question, Options


class Naurok:
    @staticmethod
    def create_session() -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            base_url="https://naurok.com.ua",
            headers=HEADERS,
            cookies=COOKIES
        )  
    
    @staticmethod
    async def search(
        session: aiohttp.ClientSession,
        subject_id: SUBJECT_LITERAL = "",
        klas: KLAS_LITERAL = 0,
        q="",
        page=1
    ) -> list[BaseTestInfo]:
        async with session.get(
            f"/test/{subject_id}{"/" if subject_id else ""}klas-{klas}",
            params={
                "q": q,
                "storinka": page
            }
        ) as req:
            soup = bs4lxml(await req.text())
        
        result: list[BaseTestInfo] = []
        for item in soup.select(".items > .file-item.test-item"):
            headline = item.select_one(".headline > a")
            name = headline.text
            href = headline.get("href", "")
            
            number_questions = int(item.select_one(".testCounter").text)

            taxonomy: list[str] = item.select_one(".taxonomy").text.strip().split(", ")
            
            subject = ""
            klass = 0
            
            try:
                subject = taxonomy[0]
            except IndexError:
                pass
            try:
                klass = int("".join(filter(lambda x: x.isdigit(), taxonomy[1])))
            except IndexError:
                pass
            
            result.append(
                BaseTestInfo(
                    name=name,
                    href=href,
                    klas=klass,
                    number_questions=number_questions,
                    subject=subject
                )
            )
            
        return result
    
    @staticmethod
    async def test_info(session: aiohttp.ClientSession, href: str) -> TestInfo:
        async with session.get(href) as req:
            soup = bs4lxml(await req.text())
        
        name = soup.select_one("div.col-md-10.col-sm-12 > h1").text
        number_questions = int("".join(filter(lambda x: x.isdigit() ,soup.select_one("div.col-md-10.col-sm-12 > div.block-head").text)))
        
        subject = ""
        klas = 0
        for item in soup.select(".breadcrumb.breadcrumb-single > span"):
            meta = item.select_one("meta")
            if meta and meta.get("content") == "2":
                subject = item.select_one("span").text
            
            if meta and meta.get("content") == "3":
                klas = int("".join(filter(lambda x: x.isdigit(), item.select_one("span").text)))
        
        questions: list[Question] = []
        for item in soup.select("div.col-md-9.col-sm-8 > .content-block.entry-item.question-view-item"):
            type = item.select_one(".option-marker")["class"][1]
            
            text = "".join(map(lambda x: str(x), item.select(".question-view-item-content p")))

            img = item.select_one("img.question-view-item-image")
            img_href = None
            if img:
                img_href = img.get("src")
            
            options: list[Options] = []
            for option in item.select(".question-options > div"):
                opt_text_ = option.select_one(".option-text > p")
                opt_text = str(opt_text_) if opt_text_ else None
                 
                opt_img  = option.select_one("img")
                opt_img_href = None
                if opt_img:
                    opt_img_href = opt_img.get("src")
                
                options.append(Options(
                    text=opt_text,
                    img=opt_img_href,
                    correctness=None
                ))
            
            questions.append(Question(
                type=type,
                text=text,
                img=img_href,
                options=options
            ))
        
        return TestInfo(
            subject=subject,
            klas=klas,
            href=(lambda u: u if "://" not in u else urlparse(u).path)(href),
            name=name,
            number_questions=number_questions,
            questions=questions
        )

    @staticmethod
    async def completed_test_info(session: aiohttp.ClientSession, href: str):
        async with session.get(href) as req:
            soup = bs4lxml(await req.text())
        
        name_test = soup.select_one(".homework-personal-stat-test").text
        number_questions = int("".join(filter(lambda x: x.isdigit(), soup.select_one(".homework-personal-stat-number").text)))
        
        questions: list[Question] = []
        for item in soup.select(".homework-stats > .content-block .homework-stat-question-line"):
            type = item.select_one(".homework-stat-option-value > span")["class"][1]
            
            text = "".join(map(lambda x: str(x), item.select(".homework-stat-question-line > p")))
            
            img = item.select_one(".col-md-6 > img")
            img_href = None
            if img:
                img_href = img.get("src")
                
            
            options: list[Options] = []
            for opt in item.select(".homework-stat-option-line .homework-stat-option-value"):
                opt_text = "".join(map(lambda x: str(x), opt.select("p")))

                opt_img = opt.select_one("img")
                opt_img_href = None
                if opt_img:
                    opt_img_href = opt_img.get("src")

                options.append(Options(
                    text=opt_text,
                    img=opt_img_href,
                    correctness=opt.select_one("span")["class"][0] == "correct",
                ))

            questions.append(Question(
                type=type,
                text=text,
                img=img_href,
                options=options
            ))
            
            
        return TestInfo(
            name=name_test,
            number_questions=number_questions,
            href=(lambda u: u if "://" not in u else urlparse(u).path)(href),
            klas=0,
            subject="",
            questions=questions
        )
    
    
async def __test():
    async with Naurok.create_session() as ses:
        data = await Naurok.completed_test_info(ses, "https://naurok.com.ua/test/complete/a7b56b11-7cc8-43e9-8326-1012e54bf346")
        print(data.model_dump_json(indent=4, ensure_ascii=False))
        # with open("output.json", "w", encoding="utf-8") as file:
        #     file.write(data.model_dump_json(indent=4, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(__test())
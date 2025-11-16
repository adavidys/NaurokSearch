from typing import Literal
from pydantic import BaseModel, field_validator

from src.utils.alias import SUBJECT_LITERAL, KLAS_LITERAL


SUBJECT_CONVERTOR = {
    'Інформатика': 'informatika',
    'Інші іноземні мови': 'inshi-inozemni-movi',
    'Іспанська мова': 'ispanska-mova',
    'Історія України': 'istoriya-ukra-ni',
    'Алгебра': 'algebra',
    'Англійська мова': 'angliyska-mova',
    'Астрономія': 'astronomiya',
    'Біологія': 'biologiya',
    'Всесвітня історія': 'vsesvitnya-istoriya',
    'Географія': 'geografiya',
    'Геометрія': 'geometriya',
    'Громадянська освіта': 'gromadyanska-osvita',
    'Екологія': 'ekologiya',
    'Економіка': 'ekonomika',
    'Етика': 'etika',
    'Зарубіжна література': 'zarubizhna-literatura',
    'Захист України': 'zahist-vitchizni',
    'Креслення': 'kreslennya',
    'Людина і світ': 'lyudina-i-svit',
    'Літературне читання': 'literaturne-chitannya',
    'Математика': 'matematika',
    'Мистецтво': 'mistectvo',
    'Мови національних меншин': 'movi-nacionalnih-menshin',
    'Музичне мистецтво': 'muzichne-mistectvo',
    'Навчання грамоти': 'navchannya-gramoti',
    'Німецька мова': 'nimecka-mova',
    'Оберіть предмет...': '',
    'Образотворче мистецтво': 'obrazotvorche-mistectvo',
    'Основи здоров’я': 'osnovi-zdorov-ya',
    'Польська мова': 'polska-mova',
    'Правознавство': 'pravoznavstvo',
    'Природничі науки': 'prirodnichi-nauki',
    'Природознавство': 'prirodoznavstvo',
    'Технології': 'tehnologi',
    'Трудове навчання': 'trudove-navchannya',
    'Українська література': 'ukrainska-literatura',
    'Українська мова': 'ukrainska-mova',
    'Французька мова': 'francuzka-mova',
    'Фізика': 'fizika',
    'Фізична культура': 'fizichna-kultura',
    'Художня культура': 'hudozhnya-kultura',
    'Хімія': 'himiya',
    'Я досліджую світ': 'ya-doslidzhuyu-svit'
}

class BaseTestInfo(BaseModel):
    subject: SUBJECT_LITERAL
    klas: KLAS_LITERAL
    
    name: str
    number_questions: int
    
    href: str
    
    @field_validator("subject", mode="before")
    def _subject(cls, value: str):
        value = value.strip()
        return SUBJECT_CONVERTOR.get(value, value)

    @field_validator("name", mode="before")
    def _name(cls, value: str):
        return value.strip()

class Options(BaseModel):
    text: str | None
    img_href: str | None
    
    @field_validator("text", mode="before")
    def _text(cls, value: str | None):
        if value is None:
            return ""
        return value.strip()
    
class Question(Options):
    type: Literal["quiz", "multiquiz"]
    options: list[Options]
    
    
class TestInfo(BaseTestInfo):
    questions: list[Question]
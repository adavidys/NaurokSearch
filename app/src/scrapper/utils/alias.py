from functools import partial
from typing import Literal

from bs4 import BeautifulSoup


bs4lxml = partial(BeautifulSoup, features="lxml")

SUBJECT_LITERAL = Literal[
    "",
    "algebra",
    "angliyska-mova",
    "astronomiya",
    "biologiya",
    "vsesvitnya-istoriya",
    "geografiya",
    "geometriya",
    "gromadyanska-osvita",
    "ekologiya",
    "ekonomika",
    "etika",
    "zarubizhna-literatura",
    "zahist-vitchizni",
    "informatika",
    "inshi-inozemni-movi",
    "ispanska-mova",
    "istoriya-ukra-ni",
    "kreslennya",
    "literaturne-chitannya",
    "lyudina-i-svit",
    "matematika",
    "mistectvo",
    "movi-nacionalnih-menshin",
    "muzichne-mistectvo",
    "navchannya-gramoti",
    "nimecka-mova",
    "obrazotvorche-mistectvo",
    "osnovi-zdorov-ya",
    "polska-mova",
    "pravoznavstvo",
    "prirodnichi-nauki",
    "prirodoznavstvo",
    "tehnologi",
    "trudove-navchannya",
    "ukrainska-literatura",
    "ukrainska-mova",
    "fizika",
    "fizichna-kultura",
    "francuzka-mova",
    "himiya",
    "hudozhnya-kultura",
    "ya-doslidzhuyu-svit"
]
KLAS_LITERAL = Literal[
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11
]

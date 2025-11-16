from pathlib import Path

from fake_useragent import UserAgent


DEBUG = True

BASE_DIR = Path()


HEADERS = {"user-agent": UserAgent().random}
COOKIES = {}


import os
import dotenv

from pathlib import Path


dotenv.load_dotenv()


DEBUG = True

BASE_DIR = Path()

POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]


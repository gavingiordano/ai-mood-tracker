import os

from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
ENV = os.environ.get("ENV", "development")
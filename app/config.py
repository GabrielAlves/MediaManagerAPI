import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///./files.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB

    API_KEY = os.getenv("API_KEY")

    STORAGE_MODE = os.getenv("STORAGE_MODE", "local")  # "local" or "s3"
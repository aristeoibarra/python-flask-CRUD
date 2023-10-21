import os
from dotenv import load_dotenv
import logging

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = os.getenv("PORT", "80")
    TESTING = os.getenv("TESTING", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = os.getenv("ENV", "production")


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_FILENAME = "app_dev.log"
    LOG_LEVEL = logging.DEBUG
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    LOG_FILENAME = "app_prod.log"
    LOG_LEVEL = logging.INFO
    ENV = "production"

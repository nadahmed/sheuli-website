from .base import *
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", '*').split(",")

MEDIA_URL = "/media/"
STATICFILES_STORAGE = "storages.backends.ftp.FTPStorage"

FTP_STORAGE_LOCATION = F"ftp://{os.getenv('FTP_USERNAME')}:{os.getenv('FTP_PASSWORD')}@{os.getenv('FTP_HOST')}:{os.getenv('FTP_PORT')}"


DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    conn_health_checks=True,
)
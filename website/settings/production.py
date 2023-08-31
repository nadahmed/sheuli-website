from .base import *
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

DEBUG = False

MEDIA_URL = "/media/"
STORAGES = {"default": {"BACKEND": "storages.backends.ftp.FTPStorage"}}

FTP_STORAGE_LOCATION = F"ftp://{os.getenv('FTP_USERNAME')}:{os.getenv('FTP_PASSWORD')}@{os.getenv('FTP_HOST')}:{os.getenv('FTP_PORT')}"


DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    conn_health_checks=True,
)
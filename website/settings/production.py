from .base import *
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

DEBUG = False

# LOGGING
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = '/debug.log'
LOG_PATH = LOG_DIR + LOG_FILE

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

if not os.path.exists(LOG_PATH):
    f = open(LOG_PATH, 'a').close() #create empty log file
else:
    f = open(LOG_PATH, 'w').close()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_PATH,
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
}


SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", '*').split(",")


DEFAULT_FILE_STORAGE = 'utils.storages.FTPMediaStorage'
STATICFILES_STORAGE = "utils.storages.FTPStaticfileStorage"

MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
STATIC_URL = os.getenv("STATIC_URL", "/static/")

FTP_STATIC_STORAGE_LOCATION = F"ftp://{os.getenv('FTP_USERNAME')}:{os.getenv('FTP_PASSWORD')}@{os.getenv('FTP_HOST')}:{os.getenv('FTP_PORT')}/{os.getenv('FTP_STATIC_DIR')}"

FTP_MEDIA_STORAGE_LOCATION = F"ftp://{os.getenv('FTP_USERNAME')}:{os.getenv('FTP_PASSWORD')}@{os.getenv('FTP_HOST')}:{os.getenv('FTP_PORT')}/{os.getenv('FTP_MEDIA_DIR')}"

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    conn_health_checks=True,
)
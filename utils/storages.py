from storages.backends.ftp import FTPStorage
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from storages.utils import setting

class FTPStaticfileStorage(FTPStorage):

    def __init__(self, location=None, base_url=None, encoding=None):
        location = location or settings.FTP_STATIC_STORAGE_LOCATION
        if location is None:
            raise ImproperlyConfigured("You must set a location at "
                                       "instanciation or at "
                                       " settings.FTP_STATIC_STORAGE_LOCATION'.")
        self.location = location
        self.encoding = encoding or setting('FTP_STORAGE_ENCODING') or 'latin-1'
        base_url = base_url or settings.STATIC_URL
        self._config = self._decode_location(location)
        self._base_url = base_url
        self._connection = None


class FTPMediaStorage(FTPStorage):
    def __init__(self, location=None, base_url=None, encoding=None):
        location = location or settings.FTP_MEDIA_STORAGE_LOCATION
        if location is None:
            raise ImproperlyConfigured("You must set a location at "
                                       "instanciation or at "
                                       " settings.FTP_MEDIA_STORAGE_LOCATION'.")
        self.location = location
        self.encoding = encoding or setting('FTP_STORAGE_ENCODING') or 'latin-1'
        base_url = base_url or settings.MEDIA_URL
        self._config = self._decode_location(location)
        self._base_url = base_url
        self._connection = None

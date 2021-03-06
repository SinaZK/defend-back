import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

#FTP_BASE_URL = 'http://dl.geogeogeo.cloud/'
FTP_BASE_URL = 'http://dl.defenddefend.com/'
#FTP_BASE_URL = 'http://130.185.79.179/'
FTP_PUBLIC_DIR = 'public_html/'

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)

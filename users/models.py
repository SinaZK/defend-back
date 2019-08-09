from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.utils import timezone

from utils.models import BaseUser

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

class Member(BaseUser):
    @property
    def token(self):
        payload = jwt_payload_handler(self)
        payload['exp'] = timezone.now() + settings.JWT_EXPIRATION_DELTA
        token = jwt_encode_handler(payload)
        
        return token

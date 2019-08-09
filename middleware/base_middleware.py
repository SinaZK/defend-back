from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            auth = JSONWebTokenAuthentication().authenticate(request)
            if auth:
                request.user = auth[0]
        except exceptions.AuthenticationFailed:
            pass
        response = self.get_response(request)
        return response

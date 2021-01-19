from rest_framework import exceptions
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication, jwt_decode_handler
import jwt


class MyAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_token = request.META.get("HTTP_AUTHORIZATION")
        token = self.parse_jwt_token(jwt_token)
        if token is None:
            return None
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed("签名已过期，请重新登录")
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("非法请求，伪造的签名")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed
        user = self.authenticate_credentials(payload)
        return user, token

    def parse_jwt_token(self, token):
        tokens = token.split()
        if len(tokens) != 3 or tokens[0].lower() != "auth" or tokens[2].lower() != "jwt":
            return None
        return tokens[1]

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.authentication import MyAuthentication
from apiapp.serializer import UserModelSerializer


class UserDetailAPIView(APIView):
    # 只允许登录之后的用户访问
    permission_classes = [IsAuthenticated]
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({
            "username": request.user.username
        })


# 实现多方式登录签发token：用户名，手机号，邮箱
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "user": UserModelSerializer(serializer.obj).data,
            "token": serializer.token
        })

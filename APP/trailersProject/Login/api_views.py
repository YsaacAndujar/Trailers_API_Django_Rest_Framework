from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class registerView(APIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        dic = {}
        if serializer.is_valid():
            user = serializer.save()
            dic.update(serializer.data)
            dic["ok"]=True
            token, created = Token.objects.get_or_create(user=user)
            dic["token"]=token.key
            return Response(dic)
        dic.update(serializer.errors)
        dic["ok"]=False
        return Response(dic)
class loginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def get(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'ok':True,
                'user': user,
                'access_token': token
            }
            return Response(data)
        dic = {}
        dic.update(serializer.errors)
        dic["ok"]=False
        return Response(dic)
        




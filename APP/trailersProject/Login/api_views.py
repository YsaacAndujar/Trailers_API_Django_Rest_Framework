from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'ok':True,
                'user': user,
                'token': token
            }
            return Response(data)
        dic = {}
        dic.update(serializer.errors)
        dic["ok"]=False
        return Response(dic)

class changePassword(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes =  [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.update(instance=request.user))
        dic = {}
        dic.update(serializer.errors)
        dic["ok"]=False
        return Response(dic)

class updateUserView(APIView):
    serializer_class = UpdateUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes =  [IsAuthenticated]
    def put(self, request):
        serializer = UpdateUserSerializer(context = {'request':request},data=request.data, instance=request.user)
        dic = {}
        if serializer.is_valid():
            serializer.update()
            dic.update(serializer.data)
            dic["ok"]=True
            return Response(dic)
        dic.update(serializer.errors)
        dic["ok"]=False
        return Response(dic)
    def get(self, request):
        serializer = UpdateUserSerializer(instance=request.user)
        dic = {}
        dic.update(serializer.data)
        dic["ok"]=True
        return Response(dic)

        




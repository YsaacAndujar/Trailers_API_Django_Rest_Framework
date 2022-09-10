from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Username or password are not valid')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        self.context['user'] = self.context['user'].get_username()
        return self.context['user'], token.key

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'email': {'default':""},
            'first_name': {'default':""},
            'last_name': {'default':""},
        }

    def create(self, validated_data):
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    oldP = serializers.CharField(write_only=True, required=True)
    newP = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('oldP', 'newP')

    def update(self, instance):
        oldP = self.validated_data["oldP"]
        print(instance.username)
        print(instance.check_password("admin123321"))
        if not instance.check_password(oldP):
            return({"ok":False,"oldP": ["Old password is not correct"]})
        instance.set_password(self.validated_data['newP'])
        instance.save()
        return {"ok":True}

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'email': {'default':""},
            'first_name': {'default':""},
            'last_name': {'default':""},
        }
    def update(self):
        instance = self.instance
        validated_data = self.validated_data
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.save()
        return instance
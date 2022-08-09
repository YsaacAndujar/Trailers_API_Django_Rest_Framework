
from django.contrib.auth.models import AbstractUser
from django.forms import EmailInput, ModelForm, TextInput

class User(AbstractUser):
    pass

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        widgets = {
            'username': TextInput(attrs={
				        'id':'account-username-input',
                    }),
            'email': EmailInput(attrs={
				        'id':'account-email-input',
                    }),
            'first_name': TextInput(attrs={
				        'id':'account-first_name-input',
                    }),
            'last_name': TextInput(attrs={
				        'id':'account-last_name-input',
                    }),
        }
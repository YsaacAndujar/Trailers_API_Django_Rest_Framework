from django.urls import path
from . import api_views
app_name="ApiLogin"
urlpatterns = [
    path('login/', api_views.loginView.as_view(), name="login"),
    path('register/', api_views.registerView.as_view(), name='register'),
    path('change-password/', api_views.changePassword.as_view(), name='changePassword'),
    path('update-user/', api_views.updateUserView.as_view(), name='updateUser'),
]
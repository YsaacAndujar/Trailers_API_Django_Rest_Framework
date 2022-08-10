from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name="Login"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('logout/', views.logoutView,name="logout"),
    path('my-account/', login_required(views.myAccount),name="myAccount"),
    path('change-password/', login_required(views.changePassword),name="changePassword"),
]
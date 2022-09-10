from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import logout
from django.urls import reverse
from .models import UserForm

# Create your views here.
def login(request):
    context={}
    if request.method=="POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except:
            context["message"]="Username and password are required"
            context["error"]=True
            return render(request,"login/login.html", context)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                if request.POST.get('rememberme', '') != 'on':
                    request.session.set_expiry(0)
                return redirect("home")
        context["message"]="Username or password are not correct"
        context["error"]=True
    return render(request,"login/login.html", context)

def logoutView(request):
    logout(request)
    return redirect("Login:login")

def myAccount(request):
    user = request.user
    context = {}
    if request.method == "POST":
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            try:
                form.save()
                context["valid"] = True
                context["form"] = form
            except Exception as e:
                context["form"]=form
                context["error"]=True
                context["errorMessage"]=e
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
        return render(request,"login/myaccount.html",context)
    context["form"] = UserForm(instance=user)
    return render(request,"login/myaccount.html", context)

def changePassword(request):
    context = {}
    if request.method == "POST":
        try:
            user = request.user
            old = request.POST["old"]
            new = request.POST["new"]
            if user.check_password(old):
                user.set_password(new)
                user.save()
                return redirect("Login:changePassword")
            return redirect(reverse("Login:changePassword")+ '?error=True&errorm=Old password is not correct')
            
        except Exception as e:
            context["error"]=True
            context["errorMessage"]=e
    else:
        try:
            if request.GET["error"]:
                context["error"]=True
                context["errorMessage"]= request.GET["errorm"]
        except:
            pass
    return render(request,"login/password.html",context)


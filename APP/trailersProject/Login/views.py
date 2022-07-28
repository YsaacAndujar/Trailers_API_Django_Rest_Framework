from django.shortcuts import redirect, render
from django.contrib import auth
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
            auth.login(request, user)
            if request.POST.get('rememberme', '') != 'on':
                request.session.set_expiry(0)
            return redirect("Home:home")
        else:
            context["message"]="Username or password are not correct"
            context["error"]=True
    return render(request,"login/login.html", context)
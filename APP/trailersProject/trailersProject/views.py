from django.shortcuts import render

def home(request):
    user = request.user
    context = {"name":user.username}
    return render(request,"index.html", context)
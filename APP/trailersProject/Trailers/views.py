from django.shortcuts import render

# Create your views here.
def add(request):
    context = {}
    return render(request, "trailers/add.html",context)
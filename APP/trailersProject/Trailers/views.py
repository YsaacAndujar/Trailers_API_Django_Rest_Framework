from django.shortcuts import render

# Create your views here.
def addTrailer(request):
    context = {}
    return render(request, "trailers/add-trailer.html",context)

def addCategory(request):
    context = {}
    return render(request, "trailers/add-category.html",context)
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def addTrailer(request):
    context = {}
    return render(request, "trailers/add-trailer.html",context)

def addCategory(request):
    context = {}

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                context["valid"] = True
                context["form"] = CategoryForm()
            except:
                context["error"]=True
                context["errorMessage"]="Try again or try again later"
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        context["form"] = CategoryForm()
    return render(request, "trailers/add-category.html",context)

def viewTrailers(request):
    context = {}
    return render(request, "trailers/view-trailers.html",context)

def viewCategories(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request, "trailers/view-categories.html",context)

def modifyCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return redirect("Trailers:viewCategories")
    context = {}
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            try:
                form.save()
                context["valid"] = True
                context["form"] = form
            except:
                context["error"]=True
                context["errorMessage"]="Try again or try again later"
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        form = CategoryForm(instance=category)
        context["form"] = form
    return render(request,"trailers/modify-category.html",context)
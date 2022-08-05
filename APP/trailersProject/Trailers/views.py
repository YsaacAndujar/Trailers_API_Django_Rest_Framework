from django.shortcuts import redirect, render
from django.urls import reverse
from .models import CategoryForm, TrailersForm, Category, Trailers
# Create your views here.
def addTrailer(request):
    context = {}
    if request.method == "POST":
        form = TrailersForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                if form.cleaned_data.get('image') is None:
                    context["error"]=True
                    context["errorMessage"]="The form is not valid"
                    context["imageError"] = "*Image file is required\n"
                    context["form"]=form
                    return render(request, "trailers/add-trailer.html",context)
                form.save()
                context["valid"] = True
                #context["form"] = TrailersForm()
                return redirect(reverse('Trailers:addTrailer') + '?valid=True')
            except Exception as e:
                context["error"]=True
                context["errorMessage"]=e
                context["form"]=form
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        context["form"] = TrailersForm()
    try:
        if request.GET["valid"]:
            context["valid"]=True
    except Exception as e:
        pass
    return render(request, "trailers/add-trailer.html",context)

def addCategory(request):
    context = {}

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('Trailers:addCategory') + '?valid=True')
            except Exception as e:
                context["form"]=form
                context["error"]=True
                context["errorMessage"]=e
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        context["form"] = CategoryForm()
    try:
        if request.GET["valid"]:
            context["valid"]=True
    except Exception as e:
        pass
    return render(request, "trailers/add-category.html",context)

def viewTrailers(request):
    trailers = Trailers.objects.all()
    context = {
        "trailers":trailers
    }
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
            except Exception as e:
                context["form"]=form
                context["error"]=True
                context["errorMessage"]=e
        else:
            context["form"]=form
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        form = CategoryForm(instance=category)
        context["form"] = form
    return render(request,"trailers/modify-category.html",context)

def modifyTrailer(request, pk):
    try:
        trailer = Trailers.objects.get(id=pk)
    except Trailers.DoesNotExist:
        return redirect("Trailers:viewTrailers")
    context = {
        "trailer":trailer
    }
    if request.method == "POST":
        form = TrailersForm(request.POST, request.FILES, instance=trailer)
        context["form"]=form
        if form.is_valid():
            try:        
                trailer2 = form.save(commit=False)
                img = request.FILES.get("image")
                if img is not None:
                    trailer2.image=img
                else:
                    trailer2.image = trailer.image
                trailer2.save()
                context["form"]=TrailersForm(instance=trailer2)
                context["trailer"]=trailer2
                context["valid"] = True
            except Exception as e:
                context["error"]=True
                context["errorMessage"]=e
        else:
            context["error"]=True
            context["errorMessage"]="The form is not valid"
    else:
        form = TrailersForm(instance=trailer)
        context["form"]=form
    return render(request, "trailers/modify-trailer.html",context)

def deleteTrailer(request, pk):
    try:
        trailer = Trailers.objects.get(id=pk)
    except Trailers.DoesNotExist:
        return redirect("Trailers:viewTrailers")
    trailer.delete()
    return redirect("Trailers:viewTrailers")
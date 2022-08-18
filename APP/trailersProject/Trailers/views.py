from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import CategoryForm, TrailersForm, Category, Trailers
from django.db.models import Case, F, FloatField, Value, When, Value
from django.db.models import Q
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
    context = { }
    trailers = Trailers.objects.all().order_by("-id")
    try:
        context["id"]=request.GET["id"]
        trailers = trailers.filter(id=context["id"])
    except:
        pass
    try:
        context["category"]=request.GET["category"]
        trailers = trailers.filter(category__in=Category.objects.filter(id=context["category"]))
    except:
        pass
    try:
        context["title"]=request.GET["title"]
        trailers=trailers.filter(Q(title__icontains=context["title"])|Q(cast__icontains=context["title"]))
        trailers = trailers.annotate(
            k1 = Case(
                When(title__icontains=context["title"], then=Value(1.0)),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            k2 = Case(
                When(title=context["title"], then=Value(1.0)),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            k3 = Case(
                When(cast__icontains=context["title"], then=Value(1.0)),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            rank= F("k1")+ F("k2")+F("k3"),
        ).order_by("-rank")
    except Exception as e:
        pass
    try:
        context["from"]=request.GET["from"]
        trailers = trailers.filter(release_date__gte=context["from"])
    except:
        pass
    try:
        context["to"]=request.GET["to"]
        trailers = trailers.filter(release_date__lte=context["to"])
    except:
        pass
    
    paginator = Paginator(trailers, 10)
    page = 1
    try:
        page = request.GET.get('page')
    except:
        pass
    trailers = paginator.get_page(page)
    categories = Category.objects.all()
    context["categories"]=categories
    context["trailers"]=trailers
    
    return render(request, "trailers/view-trailers.html",context)

def viewCategories(request):
    categories = Category.objects.all().order_by("name")
    context = {}
    try:
        context["id"]=request.GET["id"]
        categories = categories.filter(id=context["id"])
    except:
        pass
    try:
        context["name"]=request.GET["name"]
        categories=categories.filter(name__icontains=context["name"])
        categories = categories.annotate(
            k1 = Case(
                When(name__icontains=context["name"], then=Value(1.0)),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            k2 = Case(
                When(name=context["name"], then=Value(1.0)),
                default=Value(0.0),
                output_field=FloatField(),
            ),
            rank= F("k1")+ F("k2"),
        ).order_by("-rank")
    except Exception as e:
        pass
    paginator = Paginator(categories, 10)
    page = 1
    try:
        page = request.GET.get('page')
    except:
        pass
    categories = paginator.get_page(page)
    context["categories"]=categories
    return render(request, "trailers/view-categories.html",context)

def modifyCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return redirect("Trailers:viewCategories")
    context = {
        "category":category
    }
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
        return render(request,"trailers/modify-category.html",context)

    else:
        form = CategoryForm(instance=category)
        context["form"] = form

        try:
            error = request.GET["error"]
            if error:
                context["error"]=True
                context["errorMessage"]=request.GET["errorm"]
        except:
            pass

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
        try:
            error = request.GET["error"]
            if error:
                context["error"]=True
                context["errorMessage"]=request.GET["errorm"]
        except:
            pass
    return render(request, "trailers/modify-trailer.html",context)

def deleteTrailer(request, pk):
    try:
        trailer = Trailers.objects.get(id=pk)
        trailer.delete()
    except Exception as e:
        return redirect(reverse("Trailers:modifyTrailers",args=(pk,))+ '?error=True&errorm='+e)
    return redirect("Trailers:viewTrailers")

def deleteCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
    except Exception as e:
        return redirect(reverse("Trailers:modifyCategory",args=(pk,))+ '?error=True&errorm='+e)
    return redirect("Trailers:viewCategories")
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Trailers
from django.db.models import Case, F, FloatField, Value, When, Value
from django.core.paginator import Paginator
from .serializers import *
from django.db.models import Q

class previewTrailersView(APIView):
    def get(self, request):
        context = { }
        trailers = Trailers.objects.all().order_by("-id")
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
        
        paginator = Paginator(trailers, 8)
        page = 1
        try:
            page = int(request.GET.get('page'))
        except:
            pass
        trailers = paginator.get_page(page)
        context["num_pages"]=paginator.num_pages
        context["page"]=page
        context["has_previous"]=trailers.has_previous()
        if trailers.has_previous():
            context["previous_page_number"]=trailers.previous_page_number()
        context["has_next"]=trailers.has_next()
        if trailers.has_next():
            context["next_page_number"]=trailers.next_page_number()
        serializer = previewTrailersSerializer(trailers, many=True,context={'request': request})
        data={}
        data["trailers"]=serializer.data
        data["context"]=context
        data["ok"]=True
        return Response(data)

class getTrailerView(APIView):
    def get(self, request, pk):
        try:
            trailers = Trailers.objects.get(id=pk)
        except Exception as e:
            return Response({"ok":False,"message":repr(e)})
        serializer = TrailersSerializer(trailers,context={'request': request})
        data={}
        data["trailer"]=serializer.data
        data["ok"]=True
        return Response(data)

class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        data={}
        data["categories"]=serializer.data
        data["ok"]=True
        return Response(data)
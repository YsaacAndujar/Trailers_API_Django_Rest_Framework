
from rest_framework import serializers
from .models import Trailers, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class previewTrailersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailers
        fields = ["id","title","image"]

class TrailersSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Trailers
        fields = "__all__"
from django.db import models
from rest_framework.serializers import ModelSerializer

from category.models import Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'image']

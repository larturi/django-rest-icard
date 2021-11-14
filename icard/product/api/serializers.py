from django.db import models
from rest_framework.serializers import ModelSerializer

from product.models import Product
from category.api.serializers import CategorySerializer

class ProductSerializer(ModelSerializer):

    category_data = CategorySerializer(
        source='category',
        read_only=True
    )
    class Meta:
        model = Product
        fields = [
            'id', 
            'title', 
            'image', 
            'price', 
            'active', 
            'category', 
            'category_data'
        ]
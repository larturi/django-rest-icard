from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Product
from product.api.serializers import ProductSerializer

class ProductApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'active']
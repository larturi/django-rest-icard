from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from product.api.views import ProductApiViewSet

router_product = DefaultRouter()

router_product.register(
    prefix='products',
    basename='products',
    viewset=ProductApiViewSet
)
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from category.api.views import CategoryApiViewSet

router_category = DefaultRouter()

router_category.register(
    prefix='categories',
    basename='categories',
    viewset=CategoryApiViewSet
)
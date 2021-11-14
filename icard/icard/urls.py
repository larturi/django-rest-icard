# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Internal
from users.api.router import router_user
from category.api.router import router_category
from product.api.router import router_product

schema_view = get_schema_view(
   openapi.Info(
      title="iCard API Doc",
      default_version='v1',
      description="Documentación de la API de iCard",
      terms_of_service="https://leandroarturi.com",
      contact=openapi.Contact(email="lea.arturi@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include('users.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base-api/", include("basemodels.urls")),
    path("user-api/", include("user.urls")),
    path('info-api/', include('info.urls')),
    path('partnership-api/', include('partnership.urls')),
    path('blog-api/', include('blog.urls')),
    path('features-api/', include('features.urls')),
    path('cars-api/', include('cars.urls')),
    path('tours-api/', include('tours.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Journeed API",
      default_version='v1',
      description="Journeed description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.decorators import api_view
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from django.conf.urls.static import static
from django.conf import settings


@api_view(('GET',))
def hello_world(request):
        return Response({"message": "Hello, world!"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs',),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
    path('api/hello/', hello_world),
]

if settings.DEBUG:
    urlpatterns += static (
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT,
    )


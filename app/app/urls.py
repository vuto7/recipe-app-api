from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.decorators import api_view
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse


@api_view(('GET',))
def hello_world(request):
        return Response({"message": "Hello, world!"})

@api_view(('GET',))
def hello_me(request):
      me = {
            "name": "Malama",
            "age": 31,
            "sal": 1000
      }

      return JsonResponse(me)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs',),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
    path('api/hello/', hello_world),
    path('api/me/', hello_me),
    path('api/author/', include('authors.urls')),
    path('api/student/', include('students.urls'))
]

if settings.DEBUG:
    urlpatterns += static (
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT,
    )


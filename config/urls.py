
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academia.urls')),
    path('academia/', include('academia.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
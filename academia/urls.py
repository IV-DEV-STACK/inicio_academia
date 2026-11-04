from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'alunos', views.AlunoViewSet)
router.register(r'planos', views.PlanoViewSet)

app_name = 'academia'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
]

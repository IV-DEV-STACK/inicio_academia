from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno, Plano
from .serializers import AlunoSerializer, PlanoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


def home(request):
    return render(request, 'academia/home.html')

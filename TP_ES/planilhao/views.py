from django.views.generic import DetailView, ListView
from django.shortcuts import render
import json

from .models import Professores, Comentarios

def home(request):
    data = Professores.objects.all()
    data2 = json.dumps(list(Professores.objects.values()))
    return render(request, "index.html", {"profs":data, "qs_json":data2})

def about(request):
    return render(request, "sobre.html")

def detalhe_professor(request, slug):
    data = Professores.objects.get(slug=slug)
    data2 = Comentarios.objects.all()
    return render(request, "detalhe_professor.html", {"prof":data, "coment":data2})

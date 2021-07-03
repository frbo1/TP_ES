from django.views.generic import DetailView, ListView
from django.shortcuts import render

from .models import Professores, Comentarios

"""class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post"""

def home(request):
    data = Professores.objects.all()
    return render(request, "index.html", {"profs":data})
 

def detalhe_professor(request, slug):
    data = Professores.objects.get(slug=slug)
    data2 = Comentarios.objects.all()
    return render(request, "detalhe_professor.html", {"prof":data, "coment":data2})
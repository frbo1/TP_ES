from django.views.generic import DetailView, ListView
from django.shortcuts import render

from .models import Professor

"""class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post"""

def home(request):
    data = Professor.objects.all()
    return render(request, "index.html", {"profs":data})

def detalhe_professor(request, slug):
    data = Professor.objects.get(slug=slug)
    return render(request, "detalhe_professor.html", {"prof":data})
    
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
"""class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("planilhao:detail", kwargs={"slug": self.slug})"""

class Professor(models.Model):
    nome = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ("nome",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("planilhao:detail", args=[self.slug])

    

class Comentarios(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=500)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-atualizado",)

    def get_absolute_url(self):
        return reverse("planilhao:detail", args=[self.slug])

    
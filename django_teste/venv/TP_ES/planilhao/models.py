from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

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

"""
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
        ordering = ("-atualizado",)"""

"""
class Professores(models.Model):
    name = models.TextField(max_length=155)
    photo = models.BinaryField(blank=True, null=True)
    slug = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        managed = False
        db_table = 'professores'
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("planilhao:detail", args=[self.slug])


class Comentarios1(models.Model):
    prof_id = models.ForeignKey(Professores, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = 'comentarios'
        ordering = ("-atualizado",)"""


class Professores(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=155)
    photo = models.ImageField(blank=True, null=True, upload_to = "photos/")
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Professores, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("planilhao:detail", args=[self.slug])

    class Meta:
        db_table = 'professores'
        ordering = ("name",)


class Comentarios(models.Model):
    id = models.IntegerField(primary_key=True)
    prof_id = models.ForeignKey(Professores, on_delete=models.CASCADE)  
    comment = models.TextField(max_length=500)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-atualizado",)

    class Meta:
        db_table = 'comentarios'
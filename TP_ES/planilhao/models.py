from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

class Professores(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=155)
    info = models.TextField(max_length=455, default="Nada")
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

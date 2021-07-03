from django.contrib import admin

# Register your models here.

"""from .models import Post

@admin.register(Post)

class postAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}"""

from . import models

admin.site.register(models.Professores)
admin.site.register(models.Comentarios)

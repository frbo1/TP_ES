from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("planilhao.urls", namespace="planilhao")),
    path('Adriano-Alonso-Veloso/planilhao/static/image/adriano_xPw9JJi.jpg', include("planilhao.urls", namespace="adriano")),
]

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("planilhao.urls", namespace="planilhao")),
    path('Adriano-Alonso-Veloso/planilhao/static/image/adriano_xPw9JJi.jpg', include("planilhao.urls", namespace="adriano")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.urls import path

from . import views

app_name = "planilhao"

urlpatterns = [
    path('', views.home, name="homepage"),
    path("sobre/", views.about, name="about"),
    path("<slug:slug>/", views.detalhe_professor, name="detail"),
]

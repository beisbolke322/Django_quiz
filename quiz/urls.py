from django.urls import path

from . import views

urlpatterns = [
    path('', views.Klausimai.as_view()),
]

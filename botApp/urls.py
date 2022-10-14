from django.urls import path
from . import views

urlpatterns = [
    path("", views.RandomWord.as_view(), name="home"),
    path("next/<int:pk>/", views.NextWord.as_view(), name="next"),
]

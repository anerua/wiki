from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikipage, name="wikipage"),
    path("wiki/search/", views.results, name="results"),
    path("wiki/create/", views.create, name="create"),
    path("wiki/create/save/", views.save, name="save"),
    path("wiki/edit/", views.edit, name="edit"),
    path("wiki/edit/update/", views.update, name="update"),
    path("wiki/rand/", views.rand, name="rand")
]

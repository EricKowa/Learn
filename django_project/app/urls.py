from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("unde/", views.undex, name="undercover"),
    path("<int:pk>/", views.DetailView.as_view(), name="detailowitsch"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:firstdatabase_id>/numbi/", views.numbi, name="numbi"),
    path("tri/", views.tri, name="tri")
]
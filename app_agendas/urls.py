from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeViewPage.as_view(), name="Agenda"),
]

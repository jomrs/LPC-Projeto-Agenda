from django.shortcuts import render
from django.views.generic import ListView
from .models import Agenda

class HomeViewPage(ListView):
    model = Agenda
    template_name = "app_agendas/index.html"


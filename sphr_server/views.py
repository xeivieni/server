from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView
from sphr_server.models import Team, Features

class IndexView(ListView):
    template_name = "website/index.html"
    model = Features


class TeamView(ListView):
    template_name = "website/team2.html"
    model = Team


class DownloadsView(TemplateView):
    template_name = "website/downloads.html"

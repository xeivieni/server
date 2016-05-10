from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "website/index.html"


class TeamView(TemplateView):
    template_name = "website/team2.html"


class DownloadsView(TemplateView):
    template_name = "website/downloads.html"

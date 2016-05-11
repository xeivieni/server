from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^team2.html', views.TeamView.as_view(), name='team'),
    url(r'^downloads.html', views.DownloadsView.as_view(), name='downloads'),
]

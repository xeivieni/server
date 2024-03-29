from __future__ import unicode_literals

from django.db import models
from os.path import dirname, join, abspath, relpath
images_path = relpath(abspath(join(dirname(__file__), "static", "website", "images")), dirname(__file__))
photos_path = relpath(abspath(join(dirname(__file__), "static", "website", "photos")), dirname(__file__))


class Team(models.Model):
    name = models.TextField(default="team member name")
    surname = models.TextField(default="team member surname")
    picture = models.FilePathField(path=photos_path, default=abspath(join(photos_path, "default.jpg")))
    description = models.TextField(default="team member description")


class Features(models.Model):
    picture = models.FileField(upload_to=images_path)
    title = models.TextField(default="Feature title")
    subtitle = models.TextField(default="Feature subtitle")
    description = models.TextField(default="Feature description")

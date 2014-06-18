from __future__ import absolute_import
from django.db import models
import hashlib
import time


def _create_hash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return hash.hexdigest()[:-10]


class Link(models.Model):
    hash = models.CharField(max_length=10, default=_create_hash, unique=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    logo = models.URLField()
    texture = models.ForeignKey('Texture')
    color = models.CharField(max_length=6)


class Texture(models.Model):
    title = models.CharField(max_length=255, null=255)
    image = models.ImageField()

    def __str__(self):
        return self.title
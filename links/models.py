from __future__ import absolute_import
from django.db import models
import hashlib
import time
import base64
import datetime


def _create_hash():
    """This function generate 10 character long base64 hash"""
    linkhash = hashlib.sha1()
    linkhash.update(str(time.time()))
    return base64.b64encode(linkhash.digest()[-7:]).replace('=', '').replace('/', '_')


class Link(models.Model):
    hash = models.CharField(max_length=10, default=_create_hash, unique=True, editable=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    logo = models.URLField(blank=True, null=True)
    texture = models.ForeignKey('Texture', null=True, blank=True)
    color = models.CharField(max_length=6, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s (%s)" % (self.title, self.hash)


class Texture(models.Model):
    title = models.CharField(max_length=255, null=255)
    image = models.ImageField()

    def __str__(self):
        return self.title
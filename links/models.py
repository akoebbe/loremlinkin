from __future__ import absolute_import
from django.db import models
from django_extensions.db import fields as djefields
from django.templatetags.static import static
from django.forms import ModelForm


class Link(models.Model):
    hash = djefields.ShortUUIDField(max_length=10)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    logo = models.URLField(blank=True, null=True)
    texture = models.ForeignKey('Texture', related_name="links", null=True, blank=True)
    color = models.CharField(max_length=6, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s (%s)" % (self.title, self.hash)

    @models.permalink
    def get_absolute_url(self):
        return 'link-detail', [self.hash]

    def get_texture_url(self):
        if self.texture:
            return static(self.texture.image.url)
        else:
            return False

class Texture(models.Model):
    title = models.CharField(max_length=255, null=255)
    image = models.ImageField()

    def __str__(self):
        return self.title

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'description', 'logo', 'color', 'texture']



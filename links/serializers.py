from django.db import models
from models import Link
from rest_framework import serializers


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.Field(source="get_absolute_url")
    texture = serializers.Field(source="get_texture_url")

    class Meta:
        model = Link
        exclude = ('id', 'create_date')

# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import links.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=255)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(unique=True, max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.URLField(null=True)),
                ('texture', models.ForeignKey(to='links.Texture', to_field='id', null=True)),
                ('color', models.CharField(max_length=6, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

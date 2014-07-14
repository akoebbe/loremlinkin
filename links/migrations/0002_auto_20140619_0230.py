# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import links.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='create_date',
            field=models.DateTimeField(default=datetime.date(2014, 6, 19), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='hash',
            field=models.CharField(unique=True, max_length=10, editable=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='color',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='logo',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='texture',
            field=models.ForeignKey(to_field='id', blank=True, to='links.Texture', null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

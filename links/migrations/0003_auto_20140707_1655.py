# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20140619_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='hash',
            field=django_extensions.db.fields.ShortUUIDField(max_length=10, editable=False, name=b'hash', blank=True),
        ),
    ]

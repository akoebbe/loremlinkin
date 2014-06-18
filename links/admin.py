from django.contrib import admin

from links.models import Link, Texture


admin.site.register([Link, Texture])
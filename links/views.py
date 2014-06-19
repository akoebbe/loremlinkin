from __future__ import absolute_import
from django.shortcuts import render, get_object_or_404

from .models import Link


def index(request):
    return render(request, 'links/index.html')


def view(request, link_hash):
    link = get_object_or_404(Link, hash=link_hash)
    return render(request, 'links/view.html', {'link': link})
from __future__ import absolute_import
from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from .serializers import LinkSerializer
from links.models import LinkForm

from .models import Link
from .serializers import LinkSerializer


def index(request, link_hash=None):
    if request.method == 'GET':
        if link_hash:
            link = get_object_or_404(Link, hash=link_hash)
            form = LinkForm(initial={'title': link.title,
                                     'description': link.description,
                                     'logo': link.logo,
                                     'color': link.color,
                                     'texture': link.texture,
                                     })
        else:
            form = LinkForm()
    else:
        form = LinkForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            logo = form.cleaned_data['logo']
            color = form.cleaned_data['color']
            texture = form.cleaned_data['texture']

            matches = Link.objects.all().filter(title=title, description=description, logo=logo, color=color, texture=texture)

            if matches:
                print "match! ", matches[0]
                link = matches[0]
            else:
                link = Link(title=title, description=description, logo=logo, color=color, texture=texture)
                link.save()

            return redirect(link)


    return render(request, 'links/index.html', {
        'form': form,
    })


def view(request, link_hash):
    link = get_object_or_404(Link, hash=link_hash)
    return render(request, 'links/view.html', {'link': link})


class LinkViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = LinkSerializer
    model = Link
    lookup_field = 'hash'

    def create(self, request, *args, **kwargs):
        serializer = LinkSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


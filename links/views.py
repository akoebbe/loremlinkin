from __future__ import absolute_import
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from .serializers import LinkSerializer

from .models import Link
from .serializers import LinkSerializer


def index(request):
    return render(request, 'links/index.html')


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


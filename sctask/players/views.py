# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerView(viewsets.ModelViewSet):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer

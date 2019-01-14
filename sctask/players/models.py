# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=50)
	nation = models.CharField(max_length = 50)
	stats = models.URLField()

	def __str__(self):
		return self.name

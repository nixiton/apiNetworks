from django.db import models
from django import forms

import logging

# Create your models here.

logger = logging.getLogger(__name__)


"""
class Result(models.Model):
	ca = models.IntegerField(blank=False)
	margin = models.IntegerField(blank=False)
	ebitda = models.IntegerField(blank=False)
	loss = models.IntegerField(blank=False)
	year = models.IntegerField(blank=False)
	society = models.ForeignKey(Society, related_name='society',on_delete=models.CASCADE)
	class Meta:
		unique_together = ('ca', 'margin','ebitda', 'loss', 'year', 'society')

def get_or_create_sector(name):
	try:
		sector = Sector()
		sector.name = name
		sector.save()
		return sector
	except Exception as e:
		try:
			sector = Sector.objects.get(name = name)
			return sector
		except Exception as e:
			return None
"""

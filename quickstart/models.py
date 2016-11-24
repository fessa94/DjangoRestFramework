from __future__ import unicode_literals

from django.db import models

class Shisha(models.Model):
	flavour = models.TextField()
	manufacturer = models.ForeignKey('Manufacturer', related_name='+', null=True)
	quantity = models.TextField()
	strength = models.TextField()

	def __str__(self):
		return self.flavour

class Manufacturer(models.Model):
	name = models.TextField()
	vendor = models.ForeignKey('Vendor', related_name='+', null=True)
	rating = models.TextField()
	address = models.TextField()

	def __str__(self):
		return self.name

class Vendor(models.Model):
	name = models.TextField()
	address = models.TextField()

	def __str__(self):
		return self.name



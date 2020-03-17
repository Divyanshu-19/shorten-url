from django.db import models

from .utils import create_shortcode
# Create your models here.

class shortURLManager(models.Model):
	def all(self, *args, **kwargs):
		qs = super(shortURLManager, self).all(*args, **kwargs)
		qs = qs.filter(active = False)
		return qs

class shortURL(models.Model):

	url = models.CharField(max_length = 220, )
	shortcode = models.CharField(max_length = 15, blank=True, unique = True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default = True)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(shortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

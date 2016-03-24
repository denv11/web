from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.CharField(max_length=255)
	likes = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('question', kwargs={'id': self.id})

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.OneToOneField(Question)
	author = models.CharField(max_length=255)


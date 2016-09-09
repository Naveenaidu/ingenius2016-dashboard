from django.db import models

class Notification(models.Model):
	title = models.TextField(blank=True)
	data = models.TextField(blank=True)
	url = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	shown = models.BooleanField(default=True, blank=False)
	setcountdown = models.BooleanField(default=True)
	def __str__(self):
		return '%s' % self.title 

class StartTime(models.Model):
	time = models.DateTimeField(blank=True)


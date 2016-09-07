from django.db import models


class Notification(models.Model):
	title = models.TextField(blank=True)
	data = models.TextField(blank=True)
	url = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	expire_at = models.DateTimeField(blank=True)

from django.conf import settings
from django.db import models
from datetime import date

from django.utils import timezone

# Create your models here.
class Notes(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	content = models.TextField()
	created_date = models.DateField(default=date.today())
	reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return str(self.user.username)
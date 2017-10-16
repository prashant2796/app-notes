from django.conf import settings

from django.db import models

from datetime import date

from django.utils import timezone
from multiselectfield import MultiSelectField





# Create your models here.

TAGS = (('Wk/Of', 'Work/Office'),
          ('Hm', 'Home'),
          ('Sc/Co', 'School/College'),
          ('Ho', 'Hobby'))

class Checklist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30,default='',blank=True)
    created_date = models.DateField(default=timezone.now().date())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)



class Todotask(models.Model):
	checklist = models.ForeignKey(Checklist, related_name='checklists', default='', on_delete=models.CASCADE)
	task_text = models.CharField(max_length=120,null=True,blank=True)
	tick = models.BooleanField(default=False)


	def __str__(self):
		return self.task_text


	def get_text(self):
		return self.task_text

class Customtags(models.Model):
	checklist = models.ForeignKey(Checklist, related_name='custom_tags', default=0, on_delete=models.CASCADE)
	user_tag=models.CharField(max_length=50,blank=True,null=True)

	def __str__(self):
		return self.user_tag



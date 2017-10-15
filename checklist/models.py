from django.conf import settings

from django.db import models



# Create your models here.
	

# class Task(models.Model):

# 	title = models.CharField(max_length=80)

# class Checklist(models.Model):

# 	checklist = models.ForeignKey(Task, related_name='checklists',blank=True,null=True)
# 	tick = models.BooleanField(default=False)
# 	task_task = models.CharField(max_length=100,default='')

# 	class Meta:
# 		unique_together = ('tasks', 'is_completed')
# 		ordering = ['is_completed']


# 	def __str__(self):
# 		return str(self.user.username)


class Checklist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30,default='')
   

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

from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    IntegerField,
    StringRelatedField,
    SlugRelatedField,
    Field,
    MultipleChoiceField,
    HyperlinkedIdentityField,
)

import datetime
import pytz
from django.utils.timezone import utc
from django.utils import dateparse

from rest_framework.response import Response

from checklist.models import(Checklist,
	                         Todotask,
	                         Customtags)

checklist_detail_url = HyperlinkedIdentityField(
    view_name = 'myapp:checklist-detail',
    read_only = True
)


TAGS = (('Wo/Of', 'Work/Office'),
        ('Sc/Co', 'School/College'),
          ('Hm', 'Home'),
          ('Ho', 'Hobby'))
         


class ChecklistSerializer(ModelSerializer):

	class Meta:
		model = Todotask
		fields = ('tick', 'task_text')

class CustomtagSerializer(ModelSerializer):
	class Meta:
		model = Customtags
		fields = [
		    'user_tag'
		]

		

class TaskSerializer(ModelSerializer):
	url = checklist_detail_url
	alert = SerializerMethodField()

	checklists = ChecklistSerializer(many=True)
	custom_tags = CustomtagSerializer(many=True)
	tags = MultipleChoiceField(choices=TAGS, allow_blank=True)


	class Meta:
		model = Checklist
		fields = ('url','alert','title','created_date','date_modified','reminder_date','tags','custom_tags','checklists')
		

		extra_kwargs = {
		'created_date' : {'read_only': True},
		}

	def create(self, validated_data):
		checklists_data = validated_data.pop('checklists')
		custom_tags_data = validated_data.pop('custom_tags')

		checklist = Checklist.objects.create(**validated_data)
		for checklist_data in checklists_data:
		    Todotask.objects.create(checklist=checklist, **checklist_data)
		for custom_tag_data in custom_tags_data:
		    Customtags.objects.create(checklist=checklist, **custom_tag_data)
		return checklist

	


	def update(self, instance, validated_data):
		tasks_data = validated_data.pop('checklists')
		tasks = (instance.checklists).all()
		tasks = list(tasks)
		custom_tags_data = validated_data.pop('custom_tags')
		custom_tags = (instance.custom_tags).all()
		custom_tags = list(custom_tags)
		instance.title = validated_data.get('title', instance.title)
		instance.tags = validated_data.get('tags', instance.tags)
		instance.reminder_date = validated_data.get('reminder_date', instance.reminder_date)
		instance.save()

		for task_data in tasks_data:
			task = tasks.pop(0)
			task.tick = task_data.get('tick', task.tick)
			task.task_text = task_data.get('task_text', task.task_text)
			task.save()

		for custom_tag_data in custom_tags_data:
			custom_tag = custom_tags.pop(0)	
			custom_tag.user_tag = custom_tag_data.get('user_tag', custom_tag.user_tag)
			custom_tag.save()

		return instance

	def get_alert(self, obj):
		local_tz = pytz.timezone('Asia/Kolkata')
		now = datetime.datetime.utcnow().replace(tzinfo=utc).astimezone(local_tz)
		reminder = str(obj.reminder_date)
		reminder_sameformat = dateparse.parse_datetime(reminder)

		if obj.reminder_date == None:
			return False
		elif reminder_sameformat.strftime("%Y-%m-%d %H:%M:%S")  <= now.strftime("%Y-%m-%d %H:%M:%S") :
			return True
		else:
			return False


		

			






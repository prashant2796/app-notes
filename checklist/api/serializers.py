from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    IntegerField,
    StringRelatedField,
    HyperlinkedIdentityField,
)
from rest_framework.response import Response

from checklist.models import Checklist,Todotask

checklist_detail_url = HyperlinkedIdentityField(
    view_name = 'myapp:checklist-detail',
    read_only = True
)

# class ChecklistSerializer(ModelSerializer):
	
# 	todo = StringRelatedField(many=True)

# 	class Meta:
# 		model = Task
# 		fields = [
# 			'url',
# 			'title',
# 			'todo',
			
# 		]

class ChecklistSerializer(ModelSerializer):

	Task_Number = IntegerField(required=False,read_only=True)
	class Meta:
		model = Todotask
		fields = ('Task_Number','tick', 'task_text')

		





class TaskSerializer(ModelSerializer):
	url = checklist_detail_url
	checklists = ChecklistSerializer(many=True)

	class Meta:
		model = Checklist
		fields = ('url','title', 'checklists')

	def create(self, validated_data):
		checklists_data = validated_data.pop('checklists')
		checklist = Checklist.objects.create(**validated_data)
		for checklist_data in checklists_data:
		    Todotask.objects.create(checklist=checklist, **checklist_data)
		return checklist

	# def update(self, instance, validated_data):
	# 	instance.title = validated_data.get('title', instance.title)
	# 	instance.save()

	# 	checklists = validated_data.get('checklists')

	# 	if checklists:
	# 		for checklist in checklists:
	# 			checklist_id = checklist.get('id', None)
	# 			if checklist_id:
	# 				task_checklist = Todotask.objects.get(id=checklist_id, checklist=instance)
	# 				task_checklist.tick = checklist.get('tick', task_checklist.tick)
	# 				task_checklist.task_text = checklist.get('task_text', task_checklist.task_text)
	# 				task_checklist.save()
	# 			else:
	# 				Todotask.objects.create(checklist=instance, **checklist)

	# 	return instance


	


	def update(self, instance, validated_data):
		tasks_data = validated_data.pop('checklists')
		tasks = (instance.checklists).all()
		tasks = list(tasks)
		instance.title = validated_data.get('title', instance.title)
		instance.save()

		for task_data in tasks_data:
			task = tasks.pop(0)
			task.tick = task_data.get('tick', task.tick)
			task.task_text = task_data.get('task_text', task.task_text)
			task.save()
		return instance

			






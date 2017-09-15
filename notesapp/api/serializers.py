from notesapp.models import Notes
from rest_framework.serializers import ModelSerializer

#creating serializer class for notes created.
class NoteSerializer(ModelSerializer):
	class Meta:
		model = Notes #specifing the model which we want to serialize
		fields = [
			'title',
			'content',
			'created_date',
			'reminder_date',

		]

		extra_kwargs = {
        'created_date' : {'read_only': True} #created_date field can only be viewed.
        }


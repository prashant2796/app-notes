from notesapp.models import Notes
from rest_framework.serializers import(
	ModelSerializer,
	HyperlinkedIdentityField,
	MultipleChoiceField,

	) 




TAGS = (('work-office', 'Work/Office'),
		('home', 'Home'),
        ('school-college', 'School/College'), 
          ('hobby', 'Hobby'),
          ('others', 'Others'))

note_detail_url = HyperlinkedIdentityField(
    view_name = 'myapp:notes-detail',
    read_only = True
)
#creating serializer class for notes created.
class NoteSerializer(ModelSerializer):
	url = note_detail_url
	tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
	class Meta:
		model = Notes #specifing the model which we want to serialize
		fields = [
			'url',
			'title',
			'content',
			'created_date',
			'reminder_date',
			'tags',

		]

		extra_kwargs = {
        'created_date' : {'read_only': True} #created_date field can only be viewed.
        }


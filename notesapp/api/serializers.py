from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    HyperlinkedIdentityField,
    MultipleChoiceField,
)
import datetime
import pytz
from django.utils.timezone import utc
from django.utils import dateparse

from notesapp.models import Notes
TAGS = (('Work-Office', 'Work/Office'),
        ('School-College', 'School/College'),
          ('Home', 'Home'),
          ('Hobby', 'Hobby'),
          ('Others', 'Others'))

note_detail_url = HyperlinkedIdentityField(
    view_name = 'myapp:notes-detail',
    read_only = True
)
class NoteSerializer(ModelSerializer):
    alert = SerializerMethodField()
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    class Meta:
        model = Notes
        fields = [
            'url',
            'alert',
            'title',
            'content',
            'created_date',
            'reminder_date',
            'tags',
        ]

        extra_kwargs = {
        'created_date' : {'read_only': True}
        }

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
    

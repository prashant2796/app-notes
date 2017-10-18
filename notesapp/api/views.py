#from django.db.models import Q

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	DjangoFilterBackend,
	)

from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from notesapp.models import Notes
from .permissions import IsOwner

from rest_framework.response import Response
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


class NoteViewSet(ModelViewSet):
	serializer_class = NoteSerializer
	permission_classes = [IsAuthenticated,IsOwner] #only the owner who has created the notes can view this notes.class IsOwner is created in permissions.py file.
	queryset=Notes.objects.all()

	filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
	search_fields = ['title','content','tags','reminder_date']
	ordering = ('-created_date')

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)

	def list(self,request,*args,**kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = NoteSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		queryset_list = Notes.objects.filter(user=user) #get Note object associated with authenticated user
		return queryset_list



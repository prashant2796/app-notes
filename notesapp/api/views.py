from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from notesapp.models import Notes
from .permissions import IsOwner

from rest_framework.response import Response
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class NoteViewSet(ModelViewSet):
	serializer_class = NoteSerializer
	permission_classes = [IsOwner] #only the owner who has created the notes can view this notes.class IsOwner is created in permissions.py file.
	queryset=Notes.objects.all()

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
		
     #overriding method list so that note list is shown to the user who has specificly created that note
	def list(self,request,*args,**kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = NoteSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		queryset = Notes.objects.filter(user=user)
		return queryset



from rest_framework import routers
from accounts.api.views import UserRegisterViewSet
from notesapp.api.views import NoteViewSet

router = routers.SimpleRouter()
router.register(r'register', UserRegisterViewSet)
router.register(r'note', NoteViewSet)
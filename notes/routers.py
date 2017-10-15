from rest_framework import routers
from accounts.api.views import UserRegisterViewSet
from notesapp.api.views import NoteViewSet
from checklist.api.views import ChecklistViewSet

router = routers.SimpleRouter()
router.register(r'register', UserRegisterViewSet)
router.register(r'note', NoteViewSet)
router.register(r'checklist', ChecklistViewSet)
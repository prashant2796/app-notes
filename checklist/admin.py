from django.contrib import admin
from .models import( Checklist, 
	                 Todotask,
	                 Customtags)
# Register your models here.

class ChecklistModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    list_display_links = ['user', 'title']
    
    class Meta:
        model = Checklist

class TodotaskModelAdmin(admin.ModelAdmin):
    list_display = ['checklist', 'task_text', 'tick']

    class Meta:
        model = Todotask
        
class CustomtagsModelAdmin(admin.ModelAdmin):
	list_display = ['checklist', 'user_tag']

	class Meta:
		model = Customtags




admin.site.register(Checklist, ChecklistModelAdmin)
admin.site.register(Todotask, TodotaskModelAdmin)
admin.site.register(Customtags, CustomtagsModelAdmin)

# #{
#     "title": "Title is new ",
#     "reminder_date": "2017-10-17T09:32:00Z",
#     "tags": [
#        "Hm"
# ],
#    "custom_tags": [
#             {
#                 "user_tag": "tag changed AGAIN"
#             }
#         ],

#     "checklists": [
#       {
#                 "tick": true,
#                 "task_text": "new world here"
#             },
#             {
#                 "tick": true,
#                 "task_text": "Do yoga"
#             }
# ]
# }
from django.contrib import admin
from .models import Checklist, Todotask
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



admin.site.register(Checklist, ChecklistModelAdmin)
admin.site.register(Todotask, TodotaskModelAdmin)

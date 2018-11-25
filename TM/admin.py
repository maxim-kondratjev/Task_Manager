from django.contrib import admin
from TM.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'competition_date']
    search_fields = ['name', 'id']


admin.site.register(Task, TaskAdmin)

from django.contrib import admin
from TM.models import Task, Profile


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'competition_date']
    search_fields = ['name', 'id']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser', ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)

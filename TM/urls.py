from django.urls import path

from TM.views import TaskView

urlpatterns = [
    path('', TaskView.as_view(), name='task_url'),
]

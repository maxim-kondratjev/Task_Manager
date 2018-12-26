from django.urls import path

from TM.views import TaskView, TaskRemoveView, TaskJoinView, TaskLeaveView

urlpatterns = [
    path('leave/', TaskLeaveView.as_view(), name='task_leave'),
    path('remove/', TaskRemoveView.as_view(), name='task_remove'),
    path('join/', TaskJoinView.as_view(), name='task_join'),
    path('', TaskView.as_view(), name='task_url'),
]

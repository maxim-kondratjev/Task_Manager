from django.urls import path

from TM.views import TaskView, TaskListView, AllTaskListView, TaskRemoveView, TaskJoinView, TaskLeaveView

urlpatterns = [
    path('my/', TaskListView.as_view(), name='my_task_list'),
    path('all/', AllTaskListView.as_view(), name='all_task_list'),
    path('leave/', TaskLeaveView.as_view(), name='task_leave'),
    path('remove/', TaskRemoveView.as_view(), name='task_remove'),
    path('join/', TaskJoinView.as_view(), name='task_join'),
    path('', TaskView.as_view(), name='task_url'),
]

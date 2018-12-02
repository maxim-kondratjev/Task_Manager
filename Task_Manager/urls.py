"""Task_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from TM.views import TaskListView, TaskView, TMLoginView, TMLogoutView, TMRegistrationView, TaskCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks_list/', TaskListView.as_view(), name='task_list'),
    path('task/<id>/', TaskView.as_view(), name='task_url'),
    path('login/', TMLoginView.as_view(), name='login'),
    path('logout/', TMLogoutView.as_view(), name='logout'),
    path('registration/', TMRegistrationView.as_view(), name='registration'),
    path('task_creation/', TaskCreateView.as_view(), name='task_creation'),
    #path('logout/', ChatLogoutView.as_view(), name='logout'),
    #path('registration/', register_user, name='registration'),
    #path('register_user/', RegisterUser.as_view(), name='register_user'),
]

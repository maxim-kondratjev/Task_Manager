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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse

from TM.views import TMLoginView, TMLogoutView, TMRegistrationView, TaskCreateView, TaskListView, ProfileView, \
    UpdateProfileView, TaskListPageView, FastTaskCreateView
from Task_Manager import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TMLoginView.as_view(), name='login'),
    path('logout/', TMLogoutView.as_view(), name='logout'),
    path('registration/', TMRegistrationView.as_view(), name='registration'),
    path('tasks_list/<str:whose>/', TaskListView.as_view(), name='task_list'),
    path('tasks_list/<str:whose>/page/', TaskListPageView.as_view(), name='task_page'),
    path('task_creation/', TaskCreateView.as_view(), name='task_creation'),
    path('fast_task_creation/',
         FastTaskCreateView.as_view(success_url='/fast_task_creation/'),
         name='fast_task_creation'),
    path('profile/', include(('TM.profile_urls', 'P'))),
    path('<int:id>/', include(('TM.task_urls', 'TM'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


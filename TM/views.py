from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from TM.forms import LoginForm, TMRegistrationForm, TaskCreationForm
from TM.models import Task


class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/tasks.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tasks'] = Task.objects.all().order_by('id')
        return data


class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/task/task.html'

    def get_context_data(self, id, **kwargs):
        data = super().get_context_data(**kwargs)
        data['task'] = Task.objects.get(id=id)
        return data


class TMLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('task_list')


class TMLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


class TMRegistrationView(CreateView):
    form_class = TMRegistrationForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskCreateView(CreateView):
    form_class = TaskCreationForm
    template_name = 'task_creation.html'

    def get_success_url(self):
        return reverse('task_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

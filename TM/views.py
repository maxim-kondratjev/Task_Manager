from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView

from TM.forms import LoginForm, TMRegistrationForm, TaskCreationForm
from TM.models import Task

User = get_user_model()


class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/tasks.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tasks'] = Task.objects.filter(executor=self.request.user.id).order_by('id')
        return data


class AllTaskListView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/tasks.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tasks'] = Task.objects.all().order_by('id')
        return data


class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/task/task.html'

    def get_context_data(self, id, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        print(Task.objects.get(id=id).executor.values('id'))
        print(user.id)
        data['is_executor'] = False
        if Task.objects.get(id=id).executor.filter(id=user.id).exists():
            print('True')
            data['is_executor'] = True
        data['task'] = Task.objects.get(id=id)
        return data


class TaskJoinView(LoginRequiredMixin, UpdateView):
    def get(self, request, id, **kwargs):
        task = Task.objects.get(id=id)
        task.executor.add(request.user)
        return HttpResponseRedirect(reverse('TL:my_task_list'))


class TMLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('TL:my_task_list')


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


class TaskCreateView(LoginRequiredMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'task_creation.html'

    def get_success_url(self):
        return reverse('task_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskRemoveView(LoginRequiredMixin, DeleteView):
    def get(self, request, id,**kwargs):
        Task.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('TL:my_task_list'))


class TaskLeaveView(LoginRequiredMixin, UpdateView):
    def get(self, request, id, **kwargs):
        task = Task.objects.get(id=id)
        cur_exec = task.executor.get(id=request.user.id)
        task.executor.remove(cur_exec)
        return HttpResponseRedirect(reverse('TL:my_task_list'))

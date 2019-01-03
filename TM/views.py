from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.list import MultipleObjectMixin

from TM.forms import LoginForm, TMRegistrationForm, TaskCreationForm, UpdateProfileForm, TaskCreateForm
from TM.models import Task, Profile

User = get_user_model()


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list/tasks.html'
    context_object_name = "tasks"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['form_create'] = TaskCreateForm(self.request.user)
        return data

    def get_queryset(self):
        if self.kwargs['whose'] == 'my':
            return self.model.objects.filter(executor=self.request.user.id).order_by('id')
        if self.kwargs['whose'] == 'all':
            return self.model.objects.all().order_by('id')


class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'task_list/task/task.html'

    def get_context_data(self, id, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['is_executor'] = False
        data['last_executor'] = False
        task_exec = Task.objects.get(id=id).executor
        cur_user = task_exec.filter(id=user.id)
        if cur_user.exists():
            data['is_executor'] = True
            if task_exec.all().count() == 1:
                data['last_executor'] = True
        data['task'] = Task.objects.get(id=id)
        return data


class TaskJoinView(LoginRequiredMixin, UpdateView):
    def get(self, request, id, **kwargs):
        task = Task.objects.get(id=id)
        task.executor.add(request.user)
        return HttpResponseRedirect(reverse('task_list', kwargs={'whose': 'my'}))


class TMLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('task_list',  kwargs={'whose': 'my'})


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
    model = Task
    #fields = ['name', 'description', 'competition_date', 'task_image']

    def get_success_url(self):
        return reverse('task_list', kwargs={'whose': 'my'})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FastTaskCreateView(LoginRequiredMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'task_list/task_element.html'
    model = Task
    #fields = ['name', 'description', 'competition_date', 'task_image']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['element'] = Task.objects.order_by('-id')[0]
        return data

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
        return HttpResponseRedirect(reverse('task_list', kwargs={'whose': 'my'}))


class TaskLeaveView(LoginRequiredMixin, UpdateView):
    def get(self, request, id, **kwargs):
        task = Task.objects.get(id=id)
        cur_exec = task.executor.get(id=request.user.id)
        task.executor.remove(cur_exec)
        return HttpResponseRedirect(reverse('task_list', kwargs={'whose': 'my'}))


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['profile'] = Profile.objects.get(id=user.id)
        return data


class UpdateProfileView(LoginRequiredMixin, View):
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'

    def get(self, request):
        user = request.user
        form = UpdateProfileForm(initial=model_to_dict(user, fields=['avatar', 'description', 'username']))
        return render(request, 'update_profile.html', {'user': user, 'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('P:profile'))

    def get_success_url(self):
        return reverse('P: profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskListPageView(ListView):
    model = Task
    template_name = 'task_list/page.html'
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        if self.kwargs['whose'] == 'my':
            return Task.objects.filter(executor=self.request.user.id).order_by('id')
        if self.kwargs['whose'] == 'all':
            return Task.objects.all().order_by('id')
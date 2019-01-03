from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from TM.models import Task, Profile

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class TMRegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'competition_date', 'task_image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.user = user
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        task.executor.set([self.user])
        return task


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "avatar", 'description')

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super().__init__(*args, **kwargs)
            self.user = user
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})

        def save(self, commit=True):
            profile = super().save(commit=False)
            if commit:
                profile.save()
            return profile


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'competition_date', 'task_image']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        task.executor.set([self.user])
        return task


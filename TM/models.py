from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default=None, verbose_name='Аватар')

    objects = UserManager()

    class Meta:
        db_table = 'Профиль'
        verbose_name = _('Профиль пользователей')
        verbose_name_plural = _('Профили пользователей')


class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Задача')
    description = models.CharField(max_length=255, verbose_name='Описание')
    competition_date = models.DateTimeField(verbose_name='Срок выполнения')
    executor = models.ManyToManyField(Profile, verbose_name='Исполнитель')
    task_image = models.ImageField(upload_to='task_images/', blank=True, null=True,
                                   verbose_name='Изображение')

    class Meta:
        db_table = 'Задача'
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')




from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True,
                               default='avatars/default_avatar.png',
                               verbose_name='Аватар')
    description = models.CharField(max_length=255, verbose_name='О себе', blank=True, null=True)
    objects = UserManager()

    def __unicode__(self):
        return u'%s' % (self.some_field)

    class Meta:
        db_table = 'Профиль'
        verbose_name = _('Профиль пользователей')
        verbose_name_plural = _('Профили пользователей')


Profile._meta.get_field('username').verbose_name = 'Имя пользователя'


class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Задача')
    description = models.CharField(max_length=255, verbose_name='Описание')
    competition_date = models.DateTimeField(verbose_name='Срок выполнения')
    executor = models.ManyToManyField(Profile, verbose_name='Исполнитель')
    task_image = models.ImageField(upload_to='task_images/', blank=True, null=True,
                                   default='task_images/default_task_image.png',
                                   verbose_name='Изображение')

    def __unicode__(self):
        return u'%s' % (self.some_field)

    class Meta:
        db_table = 'Задача'
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')




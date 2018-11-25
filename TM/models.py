from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    competition_date = models.DateTimeField()


class Profile(AbstractUser):
    #avatar = models.FileField(blank=True, null=True, default=None, verbose_name='Аватар')

    objects = UserManager()

    class Meta:
        db_table = 'profile'
        verbose_name = _('user profile')
        verbose_name_plural = _('user profile')
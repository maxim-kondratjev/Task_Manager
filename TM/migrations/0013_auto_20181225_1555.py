# Generated by Django 2.1.4 on 2018-12-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TM', '0012_auto_20181225_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_image',
            field=models.ImageField(blank=True, default='/default_task_image.png', null=True, upload_to='task_images/', verbose_name='Изображение'),
        ),
    ]

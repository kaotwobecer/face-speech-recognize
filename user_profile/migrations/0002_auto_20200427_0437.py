# Generated by Django 3.0.5 on 2020-04-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='status',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='speech',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
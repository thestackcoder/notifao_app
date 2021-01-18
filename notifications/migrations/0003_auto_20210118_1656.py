# Generated by Django 3.0.8 on 2021-01-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_usernotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernotification',
            name='app_id',
        ),
        migrations.AddField(
            model_name='usernotification',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
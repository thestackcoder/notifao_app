# Generated by Django 3.0.8 on 2021-03-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_app_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='total_notifications_sent',
            field=models.IntegerField(default=0),
        ),
    ]

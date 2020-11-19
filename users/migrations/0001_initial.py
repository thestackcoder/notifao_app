# Generated by Django 3.0.8 on 2020-09-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='user_image/')),
            ],
        ),
    ]

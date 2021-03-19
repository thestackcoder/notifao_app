# Generated by Django 3.0.8 on 2021-03-19 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('notifications_used', models.IntegerField(default=0)),
                ('notifications_actual_used', models.IntegerField(default=0)),
                ('app_qr', models.ImageField(blank=True, upload_to='app_qr/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('app_image', models.ImageField(blank=True, upload_to='app_image/')),
                ('app_logo', models.ImageField(blank=True, upload_to='app_logo/')),
                ('app_url', models.CharField(max_length=500)),
                ('total_notifications_sent', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app', to='app.App')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.User')),
            ],
        ),
    ]

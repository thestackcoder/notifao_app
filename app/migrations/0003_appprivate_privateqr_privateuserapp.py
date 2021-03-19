# Generated by Django 3.0.8 on 2021-03-19 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_app_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateQr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('app_qr', models.ImageField(blank=True, upload_to='app_qr/')),
                ('customer_hash_code', models.CharField(max_length=500)),
                ('qr_used', models.BooleanField(default=False)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_app', to='app.App')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateUserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('Private_qr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_qr', to='app.PrivateQr')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_user', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='AppPrivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('notifications_used', models.IntegerField(default=0)),
                ('notifications_actual_used', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('app_image', models.ImageField(blank=True, upload_to='app_image/')),
                ('app_logo', models.ImageField(blank=True, upload_to='app_logo/')),
                ('app_url', models.CharField(max_length=500)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_private_app', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
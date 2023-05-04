# Generated by Django 4.2.1 on 2023-05-04 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='receive_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='send_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_users', to=settings.AUTH_USER_MODEL),
        ),
    ]

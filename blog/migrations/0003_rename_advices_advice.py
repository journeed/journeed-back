# Generated by Django 5.0.4 on 2024-06-10 11:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advices',
            new_name='Advice',
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='code',
        ),
    ]
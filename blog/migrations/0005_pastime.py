# Generated by Django 5.0.4 on 2024-06-10 12:36

import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_gallery_alter_advice_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.advice_image_uploader)),
                ('title', models.CharField(max_length=350)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Pastime',
                'verbose_name_plural': 'Pastimes',
                'ordering': ('-created_at',),
            },
        ),
    ]
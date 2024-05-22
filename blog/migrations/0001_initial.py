# Generated by Django 5.0.4 on 2024-05-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('code', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=350)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
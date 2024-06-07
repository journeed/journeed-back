# Generated by Django 5.0.4 on 2024-06-07 20:33

import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipCommissionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Partnership Commission',
                'verbose_name_plural': 'Partnership Commissions',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PartnershipFaqInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Partnership Faq',
                'verbose_name_plural': 'Partnership Faq',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PartnershipFeatureInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Partnership Feature',
                'verbose_name_plural': 'Partnership Features',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PartnershipTypeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('international', models.FloatField()),
                ('domestic', models.FloatField()),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.partnership_type_photo_uploader)),
            ],
            options={
                'verbose_name': 'Partnership Type',
                'verbose_name_plural': 'Partnership Types',
                'ordering': ('-created_at',),
            },
        ),
    ]

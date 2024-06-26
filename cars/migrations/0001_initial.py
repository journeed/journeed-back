# Generated by Django 5.0.4 on 2024-06-20 12:49

import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('person_count', models.PositiveIntegerField(default=2)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('fuel_volume', models.IntegerField()),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Car categories',
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.car_image_uploader)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'Car images',
            },
        ),
        migrations.CreateModel(
            name='CarReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(choices=[(1, '★✩✩✩✩'), (2, '★★✩✩✩'), (3, '★★★✩✩'), (4, '★★★★✩'), (5, '★★★★★')])),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'Car reviews',
            },
        ),
        migrations.CreateModel(
            name='CarWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'Car wishlist',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'fuel',
                'verbose_name_plural': 'Car fuels',
            },
        ),
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'steering',
                'verbose_name_plural': 'Steering',
            },
        ),
    ]

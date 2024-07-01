# Generated by Django 5.0.4 on 2024-07-01 20:47

import django.db.models.deletion
import phonenumber_field.modelfields
import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slogan', models.CharField(max_length=300)),
                ('head', models.CharField(max_length=300)),
                ('background', models.ImageField(null=True, upload_to=services.uploader.Uploader.about_background_uploader)),
                ('first_content', models.TextField()),
                ('second_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('request_type', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='DifferentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('head', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('head', models.CharField(max_length=200)),
                ('first_content', models.TextField(blank=True, null=True)),
                ('second_content', models.TextField(blank=True, null=True)),
                ('home_background', models.ImageField(upload_to=services.uploader.Uploader.head_background_uploader)),
                ('home_banner', models.TextField()),
                ('home_banner_background', models.ImageField(upload_to=services.uploader.Uploader.head_background_uploader)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.special_offer_image_uploader)),
                ('title', models.CharField(max_length=350)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Special Offer',
                'verbose_name_plural': 'Special Offers',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('mail', models.EmailField(max_length=254)),
                ('work_time', models.CharField(max_length=400)),
                ('map', models.URLField()),
                ('social_media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.socialmedia')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

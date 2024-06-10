# Generated by Django 5.0.4 on 2024-06-10 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_partnership': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='type_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carcategory'),
        ),
        migrations.AddField(
            model_name='carimage',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AddField(
            model_name='carreview',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AddField(
            model_name='carreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carwishlist',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AddField(
            model_name='carwishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.fuel'),
        ),
        migrations.AddField(
            model_name='car',
            name='steering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.steering'),
        ),
    ]

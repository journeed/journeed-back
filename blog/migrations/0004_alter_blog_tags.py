# Generated by Django 5.0.4 on 2024-06-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]
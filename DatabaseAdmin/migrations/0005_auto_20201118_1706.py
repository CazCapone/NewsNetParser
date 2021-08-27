# Generated by Django 3.1.3 on 2020-11-18 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseAdmin', '0004_article_date_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_sort',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
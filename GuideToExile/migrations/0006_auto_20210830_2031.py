# Generated by Django 3.2.6 on 2021-08-30 18:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0005_auto_20210830_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildguide',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]

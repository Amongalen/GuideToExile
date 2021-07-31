# Generated by Django 3.1.13 on 2021-07-31 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BuildsOfExile', '0004_auto_20210730_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile',
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]

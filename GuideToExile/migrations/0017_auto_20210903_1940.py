# Generated by Django 3.2.6 on 2021-09-03 17:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0016_auto_20210903_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ascendancyclass',
            old_name='_base_class_name',
            new_name='base_class_name',
        ),
        migrations.RenameField(
            model_name='ascendancyclass',
            old_name='_name',
            new_name='name',
        ),
    ]

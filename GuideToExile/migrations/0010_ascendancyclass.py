# Generated by Django 3.2.6 on 2021-09-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0009_auto_20210902_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='AscendancyClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('base_class_name', models.CharField(max_length=60)),
            ],
        ),
    ]
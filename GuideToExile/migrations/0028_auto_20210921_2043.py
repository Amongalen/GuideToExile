# Generated by Django 3.2.6 on 2021-09-21 18:43

from django.db import migrations


def change_user_type(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    ct = ContentType.objects.filter(
        app_label='auth',
        model='user'
    ).first()
    if ct:
        ct.app_label = 'GuideToExile'
        ct.save()


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0027_auto_20210921_1741'),
    ]

    operations = [
        migrations.RunPython(change_user_type)
    ]
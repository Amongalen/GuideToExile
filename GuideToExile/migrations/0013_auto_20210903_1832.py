# Generated by Django 3.2.6 on 2021-09-03 16:32

from django.db import migrations


def export_asc_classes(apps, schema_editor):
    AscendancyClass = apps.get_model('GuideToExile', 'AscendancyClass')
    BuildGuide = apps.get_model('GuideToExile', 'BuildGuide')
    for guide in BuildGuide.objects.all():
        asc_name = guide.pob_details.ascendancy_name
        if asc_name == 'None':
            base_class_name = guide.pob_details.class_name
            asc_class = AscendancyClass.objects.get(name='None', base_class_name=base_class_name)
        else:
            asc_class = AscendancyClass.objects.get(name=asc_name)
        guide.ascendancy_class = asc_class
        guide.save()


def revert_export_asc_classes(apps, schema_editor):
    AscendancyClass = apps.get_model('GuideToExile', 'AscendancyClass')


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0012_buildguide_ascendancy_class'),
    ]

    operations = [
        migrations.RunPython(export_asc_classes, revert_export_asc_classes)
    ]
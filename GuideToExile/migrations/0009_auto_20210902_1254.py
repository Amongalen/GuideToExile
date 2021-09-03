# Generated by Django 3.2.6 on 2021-09-02 10:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('GuideToExile', '0008_auto_20210831_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                (
                'guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GuideToExile.buildguide')),
                (
                'user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GuideToExile.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_guides',
            field=models.ManyToManyField(through='GuideToExile.GuideLike', to='GuideToExile.BuildGuide'),
        ),
        migrations.AddConstraint(
            model_name='guidelike',
            constraint=models.UniqueConstraint(fields=('guide', 'user'), name='unique_relation'),
        ),
    ]
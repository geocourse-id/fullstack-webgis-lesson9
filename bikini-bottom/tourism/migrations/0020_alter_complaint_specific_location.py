# Generated by Django 4.2.1 on 2023-05-10 18:11

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0019_alter_complaint_specific_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='specific_location',
            field=django.contrib.gis.db.models.fields.PointField(default='SRID=3857;POINT(0.0 0.0)', srid=4326),
        ),
    ]

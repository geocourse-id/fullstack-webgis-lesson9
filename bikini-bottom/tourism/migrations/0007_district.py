# Generated by Django 4.2.1 on 2023-05-06 15:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0006_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=5)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]

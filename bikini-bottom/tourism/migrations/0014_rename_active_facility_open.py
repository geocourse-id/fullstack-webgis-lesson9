# Generated by Django 4.2.1 on 2023-05-09 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0013_facility_active_alter_facility_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='active',
            new_name='open',
        ),
    ]

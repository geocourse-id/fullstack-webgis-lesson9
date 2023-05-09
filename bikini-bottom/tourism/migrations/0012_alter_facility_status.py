# Generated by Django 4.2.1 on 2023-05-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0011_alter_facility_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='status',
            field=models.CharField(choices=[('proposed', 'Proposed'), ('under review', 'Under Review'), ('planned', 'Planned'), ('cancelled', 'Cancelled'), ('constructing', 'Under Construction'), ('open', 'Service is open'), ('close', 'Service is closed')], max_length=12),
        ),
    ]

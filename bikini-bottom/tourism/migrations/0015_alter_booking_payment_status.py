# Generated by Django 4.2.1 on 2023-05-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0014_rename_active_facility_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=10),
        ),
    ]
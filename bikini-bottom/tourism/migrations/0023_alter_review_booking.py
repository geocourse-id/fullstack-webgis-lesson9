# Generated by Django 4.2.1 on 2023-05-11 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0022_alter_complaint_specific_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='booking',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tourism.booking'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0008_alter_facility_price_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='photo',
            field=models.ImageField(default='patrick.png', upload_to='facility/photo'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0017_alter_lineinfrastructure_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status_handling',
            field=models.CharField(choices=[('received', 'Received'), ('invalid', 'Invalid'), ('processed', 'Processed'), ('fixed', 'Fixed')], default='received', max_length=10),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-15 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0026_remove_review_is_recommended'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

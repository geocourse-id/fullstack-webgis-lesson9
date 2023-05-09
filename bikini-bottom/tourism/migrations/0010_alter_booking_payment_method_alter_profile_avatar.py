# Generated by Django 4.2.1 on 2023-05-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0009_facility_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer'), ('Electronic Wallet', 'Electronic Wallet')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='patrick.png', help_text='If user not upload any photo, it will automatically assign with Patrick Star', upload_to='profile/avatar'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-06 15:46

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourism', '0005_alter_profile_nationality_lineinfrastructure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('inactive', 'Inactive Service'), ('damage', 'Infrastructure Damage'), ('malfunction', 'Malfunction Service'), ('vandalism', 'Vandalism')], max_length=12)),
                ('specific_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('proof_image', models.ImageField(upload_to='complaint')),
                ('status_handling', models.CharField(choices=[('received', 'Received'), ('invalid', 'Invalid'), ('processed', 'Processed'), ('fixed', 'Fixed')], max_length=10)),
                ('comment', models.TextField()),
                ('response', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('infrastructure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.lineinfrastructure')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

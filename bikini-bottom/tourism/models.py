from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Facility(models.Model):
  class Meta:
    verbose_name = 'Facility'
    verbose_name_plural = 'Facilities'

  TYPES_CHOICES = [
    ('government', 'Government'),
    ('public', 'Public Facility'),
    ('park', 'Park'),
    ('cafe', 'Cafe'),
    ('restaurant', 'Restaurant'),
    ('parking', 'Parking Lot'),
    ('finance', 'Financial Service'),
    ('cinema', 'Cinema'),
    ('amusement', 'Amusement'),
    ('shop', 'Shop'),
    ('market', 'Market'),
    ('worship', 'Worship Place'),
    ('homestay', 'Homestay'),
    ('hotel', 'Hotel'),
    ('house', 'House'),
    ('apartment', 'Apartment'),
    ('office', 'Office'),
  ]

  STATUS_CHOICES = [
    ('proposed', 'Proposed'),
    ('constructing', 'Under Construction'),
    ('open', 'Service is open'),
    ('close', 'Service is closed'),
  ]

  PRICE_UNIT_CHOICES = [
    ('hour', 'Hourly'),
    ('hour_3', 'Per 3 hours'),
    ('hour_6', 'Per 6 hours'),
    ('hour_12', 'Per 12 hours'),
    ('day', 'Daily'),
    ('week', 'Weekly'),
    ('month', 'Monthly'),
    ('year', 'Annual'),
  ]

  name = models.CharField(max_length=80)
  types = models.CharField(max_length=10, choices=TYPES_CHOICES)
  status = models.CharField(max_length=12, choices=STATUS_CHOICES)
  location = models.PointField()
  price = models.DecimalField(max_digits=20, decimal_places=2)
  price_unit = models.CharField(max_length=10, choices=PRICE_UNIT_CHOICES)
  operator = models.ForeignKey(User, on_delete=models.CASCADE)
  
  # METADATA
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

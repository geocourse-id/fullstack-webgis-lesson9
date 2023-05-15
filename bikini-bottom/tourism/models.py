from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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
    ('under review', 'Under Review'),
    ('planned', 'Planned'),
    ('cancelled', 'Cancelled'),
    ('constructing', 'Under Construction'),
    ('complete', 'Completed'),
  ]

  PRICE_UNIT_CHOICES = [
    ('hourly', 'Hourly'),
    ('per 3 hours', 'Per 3 hours'),
    ('per 6 hours', 'Per 6 hours'),
    ('per 12 hours', 'Per 12 hours'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annual', 'Annual'),
  ]

  name = models.CharField(max_length=80)
  types = models.CharField(max_length=10, choices=TYPES_CHOICES)
  status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='proposed')
  open = models.BooleanField(default=False)
  location = models.PointField(spatial_index=True, srid=4326)
  price = models.DecimalField(max_digits=20, decimal_places=2)
  price_unit = models.CharField(max_length=12, choices=PRICE_UNIT_CHOICES)
  photo = models.ImageField(upload_to='facility/photo')
  operator = models.ForeignKey(User, on_delete=models.CASCADE)
  
  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Booking(models.Model):
  PAYMENT_METHOD_CHOICES = [
    ('Cash', 'Cash'),
    ('Bank Transfer', 'Bank Transfer'),
    ('Electronic Wallet', 'Electronic Wallet'),
  ]

  PAYMENT_STATUS_CHOICES = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
  ]

  facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
  start_visit = models.DateTimeField()
  end_visit = models.DateTimeField()
  payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
  payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.id}-{self.facility}'
  
class Review(models.Model):
  booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
  score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
  comment = models.TextField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.booking}-{self.score}'

class LineInfrastructure(models.Model):
  TYPES_CHOICES = [
    ('Highway', 'Highway'),
    ('Main Road', 'Main Road'),
    ('Local Road', 'Local Road'),
    ('Residential Road', 'Residential Road'),
    ('Inter-city Railway', 'Inter-city Railway'),
    ('Local Railway', 'Local Railway'),
    ('Canal', 'Canal'),
    ('Sewer', 'Sewer'),
    ('Power Line', 'Power Line'),
    ('Water Pipeline', 'Water Pipeline'),
    ('Telecom Line', 'Telecomunication Line'),
  ]

  STATUS_CHOICES = [
    ('proposed', 'Proposed'),
    ('under review', 'Under Review'),
    ('planned', 'Planned'),
    ('cancelled', 'Cancelled'),
    ('constructing', 'Under Construction'),
    ('complete', 'Completed'),
  ]

  name = models.CharField(max_length=80)
  types = models.CharField(max_length=20, choices=TYPES_CHOICES)
  status = models.CharField(max_length=12, choices=STATUS_CHOICES)
  geometry = models.LineStringField(spatial_index=True, srid=4326)
  operator = models.ForeignKey(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
class Complaint(models.Model):
  TYPES_CHOICES = [
    ('inactive', 'Inactive Service'),
    ('damage', 'Infrastructure Damage'),
    ('malfunction', 'Malfunction Service'),
    ('vandalism', 'Vandalism'),
  ]

  STATUS_HANDLING_CHOICES = [
    ('received', 'Received'),
    ('invalid', 'Invalid'),
    ('processed', 'Processed'),
    ('fixed', 'Fixed')
  ]

  infrastructure = models.ForeignKey(LineInfrastructure, on_delete=models.CASCADE)
  types = models.CharField(max_length=12, choices=TYPES_CHOICES)
  specific_location = models.PointField(spatial_index=True, srid=4326)
  proof_image = models.ImageField(upload_to='complaint')
  status_handling = models.CharField(max_length=10, choices=STATUS_HANDLING_CHOICES, default='received')
  comment = models.TextField()
  response = models.TextField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.infrastructure}-{self.status_handling}'
  
class District(models.Model):
  name = models.CharField(max_length=80)
  code = models.CharField(max_length=5)
  geometry = models.PolygonField(spatial_index=True, srid=4326)

  def __str__(self):
    return self.name
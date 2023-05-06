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
    ('planned', 'Planned'),
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
  location = models.PointField(spatial_index=True, srid=4326)
  price = models.DecimalField(max_digits=20, decimal_places=2)
  price_unit = models.CharField(max_length=10, choices=PRICE_UNIT_CHOICES)
  operator = models.ForeignKey(User, on_delete=models.CASCADE)
  
  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Booking(models.Model):
  PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('transfer', 'Bank Transfer'),
    ('e_wallet', 'Electronic Wallet'),
  ]

  PAYMENT_STATUS_CHOICES = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
  ]

  facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
  start_visit = models.DateTimeField()
  end_visit = models.DateTimeField()
  payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
  payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
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
  is_recommended = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.booking}-{self.score}'
  
class Profile(models.Model):
  NATIONALITY_CHOICES = [
    ('AD', 'Andorra'),
    ('AE', 'United Arab Emirates'),
    ('AF', 'Afghanistan'),
    ('AG', 'Antigua and Barbuda'),
    ('AI', 'Anguilla'),
    ('AL', 'Albania'),
    ('AM', 'Armenia'),
    ('AN', 'Netherlands Antilles'),
    ('AO', 'Angola'),
    ('AQ', 'Antarctica'),
    ('AR', 'Argentina'),
    ('AS', 'American Samoa'),
    ('AT', 'Austria'),
    ('AU', 'Australia'),
    ('AW', 'Aruba'),
    ('AZ', 'Azerbaijan'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BB', 'Barbados'),
    ('BD', 'Bangladesh'),
    ('BE', 'Belgium'),
    ('BF', 'Burkina Faso'),
    ('BG', 'Bulgaria'),
    ('BH', 'Bahrain'),
    ('BI', 'Burundi'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BN', 'Brunei'),
    ('BO', 'Bolivia'),
    ('BR', 'Brazil'),
    ('BS', 'Bahamas'),
    ('BT', 'Bhutan'),
    ('BV', 'Bouvet Island'),
    ('BW', 'Botswana'),
    ('BY', 'Belarus'),
    ('BZ', 'Belize'),
    ('CA', 'Canada'),
    ('CC', 'Cocos [Keeling] Islands'),
    ('CD', 'Congo [DRC]'),
    ('CF', 'Central African Republic'),
    ('CG', 'Congo [Republic]'),
    ('CH', 'Switzerland'),
    ('CI', 'Côte d\'Ivoire'),
    ('CK', 'Cook Islands'),
    ('CL', 'Chile'),
    ('CM', 'Cameroon'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('CR', 'Costa Rica'),
    ('CU', 'Cuba'),
    ('CV', 'Cape Verde'),
    ('CX', 'Christmas Island'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DJ', 'Djibouti'),
    ('DK', 'Denmark'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('DZ', 'Algeria'),
    ('EC', 'Ecuador'),
    ('EE', 'Estonia'),
    ('EG', 'Egypt'),
    ('EH', 'Western Sahara'),
    ('ER', 'Eritrea'),
    ('ES', 'Spain'),
    ('ET', 'Ethiopia'),
    ('FI', 'Finland'),
    ('FJ', 'Fiji'),
    ('FK', 'Falkland Islands [Islas Malvinas]'),
    ('FM', 'Micronesia'),
    ('FO', 'Faroe Islands'),
    ('FR', 'France'),
    ('GA', 'Gabon'),
    ('GB', 'United Kingdom'),
    ('GD', 'Grenada'),
    ('GE', 'Georgia'),
    ('GF', 'French Guiana'),
    ('GG', 'Guernsey'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GL', 'Greenland'),
    ('GM', 'Gambia'),
    ('GN', 'Guinea'),
    ('GP', 'Guadeloupe'),
    ('GQ', 'Equatorial Guinea'),
    ('GR', 'Greece'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('GT', 'Guatemala'),
    ('GU', 'Guam'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('GZ', 'Gaza Strip'),
    ('HK', 'Hong Kong'),
    ('HM', 'Heard Island and McDonald Islands'),
    ('HN', 'Honduras'),
    ('HR', 'Croatia'),
    ('HT', 'Haiti'),
    ('HU', 'Hungary'),
    ('ID', 'Indonesia'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IM', 'Isle of Man'),
    ('IN', 'India'),
    ('IO', 'British Indian Ocean Territory'),
    ('IQ', 'Iraq'),
    ('IR', 'Iran'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('JE', 'Jersey'),
    ('JM', 'Jamaica'),
    ('JO', 'Jordan'),
    ('JP', 'Japan'),
    ('KE', 'Kenya'),
    ('KG', 'Kyrgyzstan'),
    ('KH', 'Cambodia'),
    ('KI', 'Kiribati'),
    ('KM', 'Comoros'),
    ('KN', 'Saint Kitts and Nevis'),
    ('KP', 'North Korea'),
    ('KR', 'South Korea'),
    ('KW', 'Kuwait'),
    ('KY', 'Cayman Islands'),
    ('KZ', 'Kazakhstan'),
    ('LA', 'Laos'),
    ('LB', 'Lebanon'),
    ('LC', 'Saint Lucia'),
    ('LI', 'Liechtenstein'),
    ('LK', 'Sri Lanka'),
    ('LR', 'Liberia'),
    ('LS', 'Lesotho'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('LV', 'Latvia'),
    ('LY', 'Libya'),
    ('MA', 'Morocco'),
    ('MC', 'Monaco'),
    ('MD', 'Moldova'),
    ('ME', 'Montenegro'),
    ('MG', 'Madagascar'),
    ('MH', 'Marshall Islands'),
    ('MK', 'Macedonia [FYROM]'),
    ('ML', 'Mali'),
    ('MM', 'Myanmar [Burma]'),
    ('MN', 'Mongolia'),
    ('MO', 'Macau'),
    ('MP', 'Northern Mariana Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MS', 'Montserrat'),
    ('MT', 'Malta'),
    ('MU', 'Mauritius'),
    ('MV', 'Maldives'),
    ('MW', 'Malawi'),
    ('MX', 'Mexico'),
    ('MY', 'Malaysia'),
    ('MZ', 'Mozambique'),
    ('NA', 'Namibia'),
    ('NC', 'New Caledonia'),
    ('NE', 'Niger'),
    ('NF', 'Norfolk Island'),
    ('NG', 'Nigeria'),
    ('NI', 'Nicaragua'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('NP', 'Nepal'),
    ('NR', 'Nauru'),
    ('NU', 'Niue'),
    ('NZ', 'New Zealand'),
    ('OM', 'Oman'),
    ('PA', 'Panama'),
    ('PE', 'Peru'),
    ('PF', 'French Polynesia'),
    ('PG', 'Papua New Guinea'),
    ('PH', 'Philippines'),
    ('PK', 'Pakistan'),
    ('PL', 'Poland'),
    ('PM', 'Saint Pierre and Miquelon'),
    ('PN', 'Pitcairn Islands'),
    ('PR', 'Puerto Rico'),
    ('PS', 'Palestinian Territories'),
    ('PT', 'Portugal'),
    ('PW', 'Palau'),
    ('PY', 'Paraguay'),
    ('QA', 'Qatar'),
    ('RE', 'Réunion'),
    ('RO', 'Romania'),
    ('RS', 'Serbia'),
    ('RU', 'Russia'),
    ('RW', 'Rwanda'),
    ('SA', 'Saudi Arabia'),
    ('SB', 'Solomon Islands'),
    ('SC', 'Seychelles'),
    ('SD', 'Sudan'),
    ('SE', 'Sweden'),
    ('SG', 'Singapore'),
    ('SH', 'Saint Helena'),
    ('SI', 'Slovenia'),
    ('SJ', 'Svalbard and Jan Mayen'),
    ('SK', 'Slovakia'),
    ('SL', 'Sierra Leone'),
    ('SM', 'San Marino'),
    ('SN', 'Senegal'),
    ('SO', 'Somalia'),
    ('SR', 'Suriname'),
    ('ST', 'São Tomé and Príncipe'),
    ('SV', 'El Salvador'),
    ('SY', 'Syria'),
    ('SZ', 'Swaziland'),
    ('TC', 'Turks and Caicos Islands'),
    ('TD', 'Chad'),
    ('TF', 'French Southern Territories'),
    ('TG', 'Togo'),
    ('TH', 'Thailand'),
    ('TJ', 'Tajikistan'),
    ('TK', 'Tokelau'),
    ('TL', 'Timor-Leste'),
    ('TM', 'Turkmenistan'),
    ('TN', 'Tunisia'),
    ('TO', 'Tonga'),
    ('TR', 'Turkey'),
    ('TT', 'Trinidad and Tobago'),
    ('TV', 'Tuvalu'),
    ('TW', 'Taiwan'),
    ('TZ', 'Tanzania'),
    ('UA', 'Ukraine'),
    ('UG', 'Uganda'),
    ('UM', 'U.S. Minor Outlying Islands'),
    ('US', 'United States'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VA', 'Vatican City'),
    ('VC', 'Saint Vincent and the Grenadines'),
    ('VE', 'Venezuela'),
    ('VG', 'British Virgin Islands'),
    ('VI', 'U.S. Virgin Islands'),
    ('VN', 'Vietnam'),
    ('VU', 'Vanuatu'),
    ('WF', 'Wallis and Futuna'),
    ('WS', 'Samoa'),
    ('XK', 'Kosovo'),
    ('YE', 'Yemen'),
    ('YT', 'Mayotte'),
    ('ZA', 'South Africa'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
  ]

  birth_date = models.DateField()
  phone = models.PositiveBigIntegerField()
  address = models.CharField(max_length=80)
  nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)
  avatar = models.ImageField(upload_to='profile/avatar', default='patrick.png')
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  # Metadata
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.id}. Profile of {self.user.get_full_name()}'

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
    ('planned', 'Planned'),
    ('constructing', 'Under Construction'),
    ('open', 'Service is open'),
    ('close', 'Service is closed'),
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
  status_handling = models.CharField(max_length=10, choices=STATUS_HANDLING_CHOICES)
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
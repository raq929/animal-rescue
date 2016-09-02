from django.db import models
from localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField, USZipCodeField

class Person(models.Model):
  first_name = models.CharField(max_length=31)
  last_name = models.CharField(max_length=31)
  email1 = models.EmailField()
  email2 = models.EmailField()
  cell_phone = models.PhoneNumberField()
  home_phone = models.PhoneNumberField()
  address = models.CharField(max_length=63)
  city = models.CharField(max_length=31)
  state = models.USStateField()
  zip_code = models.USZipCodeField()
  availability = models.TextField()
  slug = '{}{}'.format(first_name, last_name)
  username = models.CharField(max_length=31)
  admin = BooleanField(default=False)

class Reference(models.Model):
  name = models.CharField(max_length=63)
  reference_type = models.CharField(max_length=31)
  checked = models.BooleanField()

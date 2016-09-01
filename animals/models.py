from django.db import models
from django.core.validators import MaxValueValidator

from people.models import Person, Reference

ADOPTED = 'A'
IN_FOSTER = 'F'
NEEDS_FOSTER = 'N'
OTHER = 'O'

STATUS_CHOICES = (
  (ADOPTED, 'Adopted'),
  (IN_FOSTER, 'In foster care'),
  (NEEDS_FOSTER, 'Needs foster'),
  (OTHER, 'Other'))

DOG = 'D'
CAT = 'C'
ANIMAL_TYPE_CHOICES = (
  (DOG, 'dog'),
  (CAT, 'cat'),
  (OTHER, 'other'))

class Animal(models.Model):
  name = models.CharField(max_length=31)
  slug = models.SlugField(
    unique=True)
  status = models.CharField(max_length=1,
                            choices=STATUS_CHOICES,
                            default=NEEDS_FOSTER)
  animal_type = models.CharField(max_length=1,
                            choices=ANIMAL_TYPE_CHOICES,
                            default=DOG)
  sex = models.BooleanField()
  breed = models.CharField(max_length=31)
  color = models.CharField(max_length=31)
  size = models.PositiveIntegerField(validators=[MaxValueValidator(300)])
  age = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
  intake_date = models.DateField()
  date_of_spay = models.DateField()
  rabies_number = models.IntegerField()
  microchip = models.CharField(max_length=31)
  vet = models.CharField(max_length=63)
  origin = models.CharField(max_length=63)
  on_petfinder = models.BooleanField()
  on_aap = models.BooleanField()
  on_facebook = models.BooleanField()
  adoption_fee = models.DecimalField(
    decimal_places=2,
    max_digits=7)
  foster = models.ForeignKey('Person',
                              models.SET_NULL,
                              blank=True,
                              null=True)
  adopter = models.ForeignKey('Person',
                              models.SET_NULL,
                              blank=True,
                              null=True)

  def __str__(self):
    return '{} {}'.format(self.name, self.pk)

  class Meta:
    ordering = ['name']

class Vaccine(models.Model):
  date = models.DateField()
  name = models.CharField(max_length=63)
  animal = models.ForeignKey(Animal,
                            on_delete=models.CASCADE)

  class Meta:
    ordering = ['animal']
    get_latest_by = 'date'


class HeartwormTest(models.Model):
  date = models.DateField()
  result = models.TextField()
  animal = models.ForeignKey(Animal,
                            on_delete=models.CASCADE)
  def __str__(self):
    return '{} - {}'.format(self.name, self.animal)

  class Meta:
    ordering = ['animal']
    get_latest_by = 'date'

class Note(models.Model):
  title = models.CharField(max_length=63, default='Note')
  written_by = models.ForeignKey('Person',
                              on_delete=models.CASCADE)
  about_animal = models.ForeignKey(Animal,
                            on_delete=models.CASCADE,
                            blank=True)
  about_reference = models.ForeignKey(Reference,
                                      on_delete=models.CASCADE,
                                      blank=True)
  text = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.name, self.modified_date)

  class Meta:
    ordering = ['about_animal', 'about_reference']
    get_latest_by = 'modified_date'







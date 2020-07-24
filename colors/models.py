from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Color(models.Model):
  name_en = models.CharField(max_length=50)
  name_ja = models.CharField(max_length=50)
  description_en = models.CharField(max_length=200)
  hex_code = models.CharField(max_length=6)

  def __str__(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 

class PigmentType(models.Model):
  code = models.CharField(max_length=2, primary_key=True)
  name_en = models.CharField(max_length=50)
  name_ja = models.CharField(max_length=50)
  description_en = models.CharField(max_length=200)

  def __str__(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 

class Pigment(models.Model):
  color = models.ForeignKey(Color, on_delete=models.CASCADE)
  pigment_type = models.ForeignKey(PigmentType, on_delete=models.CASCADE)
  hex_code = models.CharField(max_length=6)
  price = models.IntegerField(default=0)

  class Grain(models.TextChoices):
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
    THIRTEEN = '13'
    BYAKU = '白' 

  grain = models.CharField(
    max_length=2,
    choices=Grain.choices,
    default=Grain.TWELVE)

  def __str__(self):
    return '{0} {1} {2}'.format(self.pigment_type, self.color, self.grain) 

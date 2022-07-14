from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class ColorFamily(models.Model):
  name_en = models.CharField(max_length=50)
  name_ja = models.CharField(max_length=50)
  hex_color = ColorField(default='#ffffff')
  order = models.IntegerField()
  
  def name(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 

  def __str__(self):
    return '{0} {1} {2}'.format(self.name_ja, self.name_en, self.hex_color) 

class Color(models.Model):
  name_en = models.CharField(max_length=50)
  name_ja = models.CharField(max_length=50)
  description_en = models.CharField(max_length=200)
  hex_color = ColorField(default='#ffffff')
  color_family = models.ForeignKey('ColorFamily', on_delete=models.CASCADE, default=0)
  dark_mode = models.BooleanField(default=False)

  def name(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 

  def __str__(self):
    return '{0} {1} {2}'.format(self.name_ja, self.name_en, self.hex_color) 

class Pigment(models.Model):
  color = models.ForeignKey(Color, on_delete=models.CASCADE)
  category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
  grain = models.ForeignKey('grains.Grain', on_delete=models.CASCADE, )
  hex_color = ColorField(default='#ffffff')
  price = models.IntegerField(default=0)
  dark_mode = models.BooleanField(default=False)

  def __str__(self):
    return '{0} {1} ({2}) {3}'.format(self.category, self.color.name(), self.grain, self.hex_color) 

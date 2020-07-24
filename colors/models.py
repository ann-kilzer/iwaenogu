from django.db import models

# Create your models here.
class Color(models.Model):
  name_en = models.CharField(max_length=50)
  name_ja = models.CharField(max_length=50)
  description_en = models.CharField(max_length=200)
  hex_code = models.CharField(max_length=6)

  def __str__(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 

class Pigment(models.Model):
  color = models.ForeignKey(Color, on_delete=models.CASCADE)
  category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
  grain = models.ForeignKey('grains.Grain', on_delete=models.CASCADE, )
  hex_code = models.CharField(max_length=6)
  price = models.IntegerField(default=0)

  def __str__(self):
    return '{0} {1}'.format(self.category, self.color) 

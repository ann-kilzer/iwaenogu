from django.db import models

# Create your models here.

class Grain(models.Model):
  label = models.CharField(max_length=2)

  def __str__(self):
      return self.label 


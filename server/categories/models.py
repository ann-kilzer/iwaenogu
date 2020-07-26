from django.db import models

# Create your models here.
class Category(models.Model):
  code = models.CharField(max_length=2, primary_key=True)
  name_en = models.CharField(max_length=20, unique=True)
  name_ja = models.CharField(max_length=20, unique=True)
  description_en = models.CharField(max_length=200)

  def __str__(self):
    return '{0} {1}'.format(self.name_ja, self.name_en) 
from django.db import models

# Create your models here.
class Iwaenogu(models.Model):
    name_en = models.CharField(max_length=50)
    name_ja = models.CharField(max_length=50)

class Grain(models.Model):
    question = models.ForeignKey(Iwaenogu, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    hex_code = models.CharField(max_length=6)
    price = models.IntegerField(default=0)

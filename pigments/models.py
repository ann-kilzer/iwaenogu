from django.db import models

# Create your models here.
class Enogu(models.Model):
    name_en = models.CharField(max_length=50)
    name_ja = models.CharField(max_length=50)

  class PigmentType(models.TextChoices):
    TENNEN_IWA = 'TI', _('Tennen Iwaenogu 天淵岩絵具')
    SHIN_IWA = 'SI', _('Shin Iwaenogu　新岩絵具')
    KYOJYO_IWA = 'KI', _('Kyojyo Iwaenogu')
    GOFUN = 'SG', _('Suihui Gofun')
    SUIHUI = 'HH', _('Suihui Enogu')
    TENNEN_TSUCHI = 'TT', _('Tennen Tsuchi Enogu　天淵土絵具')

    pigment_type = models.CharField(
      max_length=2,
      choices=PigmentType.choices)

class Grain(models.Model):
    question = models.ForeignKey(Iwaenogu, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    hex_code = models.CharField(max_length=6)
    price = models.IntegerField(default=0)

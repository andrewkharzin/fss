from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _


class Airline(models.Model):
    airline_name = models.CharField(
        _("Airline name"), max_length=50, default='')
    description_rus = models.CharField(max_length=255, default='')
    iata_code = models.CharField(max_length=2, default='')
    icao_code = models.CharField(max_length=3, default='')
    rus_code = models.CharField(max_length=2, default='')
    country = models.CharField(max_length=155, default='')
    alliance = models.CharField(max_length=155, default='')

    def __str__(self):
        return self.iata_code

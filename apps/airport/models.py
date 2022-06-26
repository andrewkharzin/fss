from django.db import models
from django.forms import IntegerField


class Airport(models.Model):
    iata_code = models.CharField(
        max_length=3, default='', null=True, blank=True)
    icao_code = models.CharField(
        max_length=4, default='', null=True, blank=True)
    rus_code = models.CharField(
        max_length=3, default='', null=True, blank=True)
    comment_eng = models.CharField(
        max_length=155, default='', null=True, blank=True)
    comment_rus = models.CharField(
        max_length=155, default='', null=True, blank=True)
    country = models.CharField(
        max_length=155, default='', null=True, blank=True)
    city_rus = models.CharField(
        max_length=155, default='', null=True, blank=True)
    s_utc = models.IntegerField(default='', null=True, blank=True)
    w_utc = models.IntegerField(default='', null=True, blank=True)
    airport_eng = models.CharField(
        max_length=155, default='', null=True, blank=True)
    region = models.CharField(
        max_length=155, default='', null=True, blank=True)
    airport_rus = models.CharField(
        max_length=155, default='', null=True, blank=True)
    comment_chn = models.CharField(
        max_length=155, default='', null=True, blank=True)
    city_eng = models.CharField(
        max_length=155, default='', null=True, blank=True)

    def __str__(self):
        return f"{self.iata_code} - (icao){self.icao_code}"

    def short_name(self):
        return f"{self.city_rus}/{self.iata_code}-{self.comment_eng}"

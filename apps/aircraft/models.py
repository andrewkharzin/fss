from django.db import models


class Aircraft(models.Model):

    iata_code = models.CharField(
        max_length=3, default='', blank=True, null=True)
    icao_code = models.CharField(
        max_length=15, default='', blank=True, null=True)
    rus_code = models.CharField(
        max_length=15, default='', blank=True, null=True)
    description_eng = models.CharField(
        max_length=255, default='', blank=True, null=True)
    description_rus = models.CharField(
        max_length=255, default='', blank=True, null=True)
    wingspan = models.CharField(
        max_length=10, default='', blank=True, null=True)
    length = models.CharField(max_length=10, default='', blank=True, null=True)
    helicopter = models.CharField(
        max_length=1, default='', blank=True, null=True)
    public_name_rus = models.CharField(
        max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return self.iata_code

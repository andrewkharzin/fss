from django.db import models
from cities.models import BaseCountry


class Country(BaseCountry, models.Model):
    more_data = models.TextField()

    class Meta(BaseCountry.Meta):
        pass

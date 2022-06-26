import uuid
from django.urls import reverse
from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.airline.models import Airline
from apps.aircraft.models import Aircraft


class FlightUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Flight(FlightUUIDModel):
    ARRIVAL = 'ARR'
    DEPARTURE = 'DEP'
    FLIGHT_KIND = (
        (ARRIVAL, _('ARR')),
        (DEPARTURE, _('DEP'))
    )

    # flight_id = models.AutoField(
    #     primary_key=True, unique=True)

    flight_date = models.DateField(
        _("Flight Date"), auto_now=False, auto_now_add=False, default='')
    flight_co = models.ForeignKey((Airline), on_delete=models.CASCADE)
    flight_kind = models.CharField(
        choices=FLIGHT_KIND, default='', max_length=10)
    flight_number = models.CharField(
        _("Flight Number"), max_length=4, default='')
    flight_ac_type = models.ForeignKey(
        (Aircraft), on_delete=models.CASCADE, default='')
    flight_ac_reg_number = models.CharField(
        _("Aircraft Registration"), max_length=5, blank=True, null=True, default='')
    # flight_route_iata = models.CharField(
    #     max_length=3, blank=True, null=True, default='')
    # flight_route_icao = models.CharField(
    #     max_length=4, blank=True, null=True, default='')
    # flight_route = models.CharField(
    #     max_length=55, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.flight_kind.upper()} -> {self.flight_co}{self.flight_number}/{self.flight_date.strftime('%d-%m-%Y')} | {self.flight_ac_type}"

    # def get_absolute_url(self):
    #     return reverse('flight_detail', args=[str(self.id)])

import uuid
from django.db import models
from django.forms import TimeField
from django.utils.translation import gettext_lazy as _
from apps.flight.models import Flight
from apps.airline.models import Airline
from apps.airport.models import Airport


class SchedPlanUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Plan(SchedPlanUUIDModel):
    STANDBY = 'Standby'
    CANCELED = 'Canceled'
    IN_PROGRESS = 'In_progress'
    NEW = 'New'
    OFFLOADING = 'Offloading'
    ONLOADING = 'Onloading'
    TECHSTOP = 'Techstop'
    TASK_STATUS = (
        (STANDBY, _('Standby')),
        (CANCELED, _('Canceled')),
        (IN_PROGRESS, _('In_progress')),
        (NEW, _('New'))
    )
    TASK_TYPE = (
        (OFFLOADING, _('Offloading')),
        (ONLOADING, _('Onloading')),
        (TECHSTOP, _('Techstop')),
    )
    task_type = models.CharField(
        _("Handling Type"), choices=TASK_TYPE, default='', max_length=50)
    task_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    task_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE)
    route_from = models.ForeignKey(Airport,  on_delete=models.CASCADE)
    flight_sta = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default='')
    task_info = models.CharField(_("Plan Info"), max_length=50, default='')
    task_status = models.CharField(
        choices=TASK_STATUS, default='New', max_length=15)
    task_approved = models.BooleanField(default=False)
    task_completed = models.BooleanField(default=False)
    task_addtime = models.DateTimeField(
        _("Created"), auto_now=True, auto_now_add=False)
    task_updatetime = models.DateTimeField(_("Update"), auto_now_add=True)
    flight_route_iata_from = models.CharField(
        max_length=3, blank=True, null=True, default='')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.task_flight}"

    # def get_type(self):
    #     return self.task_type.upper()
    def get_task_date(self):
        return self.task_date.strftime('%d/%m/%Y')

    def STA(self):
        return self.flight_sta.strftime('%H:%m')

    def create_datetime(self):
        return self.task_addtime.strftime('%d/%m - %H:%m')

    def update_datetime(self):
        return self.task_updatetime.strftime('%d/%m - %H:%m')

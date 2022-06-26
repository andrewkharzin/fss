from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'flight_kind',
        'flight_date',
        'flight_co',
        'flight_number',
        'flight_ac_type',
        'flight_ac_reg_number',





    ]


class FlightAdmin(admin.ModelAdmin):
    exclude = ['id']

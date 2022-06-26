from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Airline

# Register your models here.


@admin.register(Airline)
class AirlineAdmin(ImportExportModelAdmin):
    list_display = [
        'airline_name',
        'description_rus',
        'iata_code',
        'icao_code',
        'rus_code',
        'country',
        'alliance',



    ]

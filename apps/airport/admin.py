from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Airport

# Register your models here.


@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    list_display = [
        'short_name',
        'iata_code',
        'icao_code',
        'rus_code',
        'comment_eng',
        'comment_rus',
        'country',
        'city_rus',
        's_utc',
        'w_utc',
        'airport_eng',
        'region',
        'airport_rus',
        'comment_chn',
        'city_eng',

     ]

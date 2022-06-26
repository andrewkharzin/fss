from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Aircraft

# Register your models here.


@admin.register(Aircraft)
class AircraftAdmin(ImportExportModelAdmin):
    # prepopulated_fields = {"slug": ("icao_code", )}
    list_display = [
        'iata_code',
        'icao_code',
        'rus_code',
        'description_eng',
        'description_rus',
        'wingspan',
        'length',
        'helicopter',
        'public_name_rus',
    ]

from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("task_flight", )}
    list_display = [
        'task_type',
        'get_task_date',
        'task_flight',
        'route_from',
        'STA',
        'task_status',
        'task_approved',
        'task_completed',
        'task_info',
        'task_addtime',
        'update_datetime',


    ]
    # readonly_fields = [
    #     'task_flight',
    # ]
    list_display_links = [
        'task_type',
        'task_flight',
    ]

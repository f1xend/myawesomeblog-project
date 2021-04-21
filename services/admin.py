from django.contrib import admin

# Register your models here.
from .models import Service, Schedule, Profile, ServiceBooking

admin.site.register(Service)

# class ScheduleInLine(admin.TabularInline):
# 	model = Schedule
# 	extra = 0

class ScheduleAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,  {'fields': ['schedule_date']}),
        (None,  {'fields': ['schedule_timefrom']}),
        (None,  {'fields': ['schedule_timeto']}),
        (None,  {'fields': ['schedule_waiting_status']}),
        (None,  {'fields': ['schedule_notes']}),
    ]
	list_display = ('schedule_date', 'schedule_timefrom', 'schedule_timeto', 'schedule_waiting_status','schedule_notes',)
	list_display_links = ('schedule_date',)
	list_editable = ('schedule_timefrom', 'schedule_timeto', 'schedule_waiting_status', 'schedule_notes',)	

admin.site.register(Schedule, ScheduleAdmin)

admin.site.register(Profile)

admin.site.register(ServiceBooking)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ['schedule_date', 'schedule_timefrom', 'schedule_timeto', 'notes', 'schedule_waiting_status']

# admin.site.register(Schedule)

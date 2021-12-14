from django.contrib import admin

from .models import Space, SpaceBooking


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(SpaceBooking)
class SpaceBooking(admin.ModelAdmin):
    list_display = ('space', 'start_of_booking', 'end_of_booking', 'employee')

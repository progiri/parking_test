from django.db import models
from django.db.models.fields.related import OneToOneField


class Space(models.Model):
    number = models.PositiveIntegerField(
        unique=True
    )

    def __str__(self) -> str:
        return str(self.number)



class SpaceBooking(models.Model):
    space = models.ForeignKey(
        to=Space,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    employee = models.ForeignKey(
        to='accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='booked_places'
    )
    start_of_booking = models.DateTimeField()
    end_of_booking = models.DateTimeField()

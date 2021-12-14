from .models import SpaceBooking


def check_bookings(space, start_time, end_time):
    space_booking = SpaceBooking.objects.all()

    booking_filter_1 = space_booking.filter(
        space=space,
        start_of_booking__lte=start_time,
        end_of_booking__gte=end_time
    )
    booking_filter_2 = space_booking.filter(
        space=space,
        end_of_booking__lte=end_time
    ).filter(
        end_of_booking__gte=start_time
    )
    booking_filter_3 = space_booking.filter(
        space=space,
        start_of_booking__gte=start_time
    ).filter(
        start_of_booking__lte=end_time
    )

    return bool(
        not booking_filter_1 and
        not booking_filter_2 and
        not booking_filter_3
    )


def create_booking(space, start_time, end_time, user):
    return SpaceBooking.objects.create(
        space=space,
        employee=user,
        start_of_booking=start_time,
        end_of_booking=end_time
    )
    

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.parking.models import Space, SpaceBooking
from apps.parking.utils import check_bookings, create_booking
from apps.accounts.permissions import IsManager, IsManagerOrReadOnly

from .serializers import SpaceSerializer, SpaceBookingSerializer


class SpacesListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsManagerOrReadOnly)
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()


class SpaceDestroyView(generics.DestroyAPIView):
    permission_classes = (IsManager,)
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()


class SpaceBookingView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        if start_time is None and end_time is None:
            return NotFound()
        else:
            space = Space.objects.get(pk=pk)
            check_booking = check_bookings(space, start_time, end_time)

            if check_booking:
                booking = create_booking(space, start_time, end_time, request.user)

                return Response({
                    "success": True,
                    "space": booking.space.number,
                    "start_time": booking.start_of_booking,
                    "end_time": booking.end_of_booking
                })

            else:
                return Response({
                    "success": False,
                    "response": "Space already booked"
                })


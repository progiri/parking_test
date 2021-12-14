from django.urls import path

from .views import SpaceBookingView, SpaceDestroyView, SpacesListView

urlpatterns = [
    path('spaces/', SpacesListView.as_view()),
    path('spaces/<int:pk>/', SpaceBookingView.as_view()),
    path('spaces/<int:pk>/delete/', SpaceDestroyView.as_view())
]
from django.urls import path
from . views import FlightListView, FlightDetailView, FlightCreateView, FlightUpdateView, FlightDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='club-home'),
    path('flights-list/', FlightListView.as_view(), name='flights-list'),
    path('flights-list/new/', FlightCreateView.as_view(), name='flight-create'),
    path('flights-list/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
    path('flights-list/<int:pk>/update/', FlightUpdateView.as_view(), name='flight-update'),
    path('flights-list/<int:pk>/delete/', FlightDeleteView.as_view(), name='flight-delete'),
]



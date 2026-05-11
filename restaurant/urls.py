from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking',views.BookingView.as_view(), name='booking' ),
    path('booking/<int:pk>', views.BookingDetailsView.as_view(), name='booking_details'),

    path('menu', views.MenuView.as_view(), name='Menu'),
    path('menu/<int:pk>', views.MenuDetailsView.as_view(), name='menu_details')
]
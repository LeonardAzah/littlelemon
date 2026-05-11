from django.test import TestCase
from restaurant.models import Booking, Menu

class BookingTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create( 
            title='icecream',
            price=200,
            inventory=100
        )
        self.assertEqual(str(item), 'icecream')
    
    def test_get_booking(self):
        booking = Booking.objects.create(
            name="Frida",
            no_of_guests=5
        )

        self.assertEqual(str(booking), 'Frida')

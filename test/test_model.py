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
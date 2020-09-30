from django.test import TestCase
from django.urls import reverse

from .models import Artist, Contact, Booking, Album

# Create tests

# Index page
class IndexPageTest(TestCase):
    # test if return status_code equal 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# Test detail page
class TestDetailPage(TestCase):
    # this method is execute before running test
    def setUp(self):
        album_test = Album.objects.create(title='Test album')
        self.album= Album.objects.get(title='Test album')

    # check if page return 200 if item exists
    def test_detail_page(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:details', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test page return error 404 if item not exists
    def test_detail_page_returns_404(self):
        album_id = self.album.id + 2
        response = self.client.get(reverse('store:details', args=(album_id,)))
        self.assertEqual(response.status_code, 404)

# Booking page
class TestBookingPage(TestCase):

    def setUp(self):
        Contact.objects.create(name='kevinoh', email='kevin@gmail.com')
        album_test = Album.objects.create(title='Test album')
        journey = Artist.objects.create(name='Journey')
        album_test.artists.add(journey)
        self.album = Album.objects.get(title='Test album')
        self.contact = Contact.objects.get(name='kevinoh')

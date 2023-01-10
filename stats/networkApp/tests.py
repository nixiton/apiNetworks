from django.test import TestCase, TransactionTestCase, Client

from urllib.parse import urlparse

from django.urls import reverse, resolve


# Create your tests here.

from .models import *

from .views import *

from .services import *



"""
# Tests urls 

class UrlsTest(TransactionTestCase ):

	def setUp(self):
		pass
	
	def test_urlstesting(self):
		url = reverse('initDbApi')
		self.assertEqual(resolve(url).func.view_class, FetchingAPI)
		url = reverse('listApi')
		self.assertEqual(resolve(url).func.view_class, ListAPI)
		url = reverse('detailApi')
		self.assertEqual(resolve(url).func.view_class, DetailAPI)



# Tests models



class ModelsTest(TransactionTestCase ):
    def setUp(self):
    	self.sector = get_or_create_sector("testSector")

    def test_get_or_create_sector(self):
    	self.sector = get_or_create_sector("testSector")
    	self.assertEqual(self.sector.name, "testSector")
	

    def test_get_or_create_society(self):
    	society = get_or_create_society("Name test1", self.sector, 12345678)
    	self.assertEqual(society.siren, 12345678)

# Tests views



class ViewsTest(TransactionTestCase ):

	def setUp(self):
		self.client = Client()
		self.client.get(reverse('initDbApi'))

	def test_fetchingAPI_get(self):
		result = self.client.get(reverse('initDbApi'))
		self.assertEqual(result.status_code, 200)


	def test_detailAPI_get_error(self):
		result = self.client.get(reverse('detailApi'), data={'id':"-1"})
		self.assertEqual(result.status_code, 500)

	def test_listAPI_get(self):
		result = self.client.get(reverse('listApi'))
		self.assertGreater(len(result.data), 0)
		self.assertEqual(result.status_code, 200)

"""



"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """ Tests that 1 + 1 always equals 2. """
        self.assertEqual(1 + 1, 2)

class LinksTestCase(TestCase):
    def test_index(self):
    	""" Tests that index page loads correctly and receives a list of furniture types. """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('types' in resp.context)
        self.assertEqual(resp.templates[0].name, 'index.html')

    def test_about(self):
    	'''Test correct linkage of about page.'''
        resp = self.client.get('/about')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'about.html')

    def test_cat_correct(self):
    	'''Test correct linkage of a category page.'''
        resp = self.client.get('/08')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'type.html')

    def test_cat_correct_2(self):
    	'''Test correct linkage of a category page.'''
        resp = self.client.get('/01')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'type.html')

    def test_cat_fail(self):
    	'''Test failing linkage of a category page.'''
        resp = self.client.get('/09')
        self.assertEqual(resp.status_code, 404)
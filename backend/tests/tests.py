from django.test import TestCase

class EntryModelTest(TestCase):
    fixtures = ['tests/fixtures/ad.json']
    def test_url_exists(self):
        response = self.client.get("/api/ad/")
        self.assertEqual(response.status_code, 200)

    def test_post_functions(self):
        response = self.client.post('/api/ad/',{
            'id':'',
            'image':'Man.jpg',
            'URL':'www.test1.com',
            'adTitle':'test1',
            'adInfo':'this is test1',
        })
        self.assertEqual(response.status_code, 201)
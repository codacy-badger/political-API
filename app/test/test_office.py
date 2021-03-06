import json
import unittest


from app.test.base_test import PoliticoV1BaseTest


class PoliticoV1BaseTest(PoliticoV1BaseTest):
    """Tests functionality of the politico office endpoint"""

    def test_create_an_office(self):
        response = self.client().post('/api/v1/office', data=self.add_office, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_office_by_id(self):
        """Tests API can get a specific office by using its id"""

        self.client().post('/api/v1/office', data=self.add_office, content_type='application/json')
        response = self.client().get('/api/v1/office/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_all_offices(self):
        """Tests API can get all offices"""
        offices = {"offices": "offices"}
        response = self.client().get('/api/v1/office', data=offices,
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

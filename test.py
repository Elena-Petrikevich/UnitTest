import unittest
from app import app

class TrigFunctionsTestCase(unittest.TestCase):

    def test_sin_degrees(self):
        with app.test_client() as client:
            response = client.post('/', data={
                'angle': '30',
                'unit': 'градусы',
                'function': 'sin',
                'precision': '3'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'0.5', response.data)

    def test_cos_radians(self):
        with app.test_client() as client:
            response = client.post('/', data={
                'angle': '45',
                'unit': 'радианы',
                'function': 'cos',
                'precision': '2'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'0.53', response.data)

    def test_tan_degrees(self):
        with app.test_client() as client:
            response = client.post('/', data={
                'angle': '-90',
                'unit': 'градусы',
                'function': 'tan',
                'precision': '5'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'-1.633123935319537e+16', response.data)


if __name__ == "__main__":
    unittest.main()
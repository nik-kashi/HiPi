import unittest

from webservices.webservices import getOutdoorTemprature


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertGreater(int(getOutdoorTemprature()), -20)
        self.assertLess(getOutdoorTemprature(), 40)


if __name__ == '__main__':
    unittest.main()

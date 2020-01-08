import unittest
import download_rocket_launches

class MyTestCase(unittest.TestCase):
    def test_something(self):
        download_rocket_launches._get_pictures()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

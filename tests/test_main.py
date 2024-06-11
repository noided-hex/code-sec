import unittest
from src.main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()

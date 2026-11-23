import unittest

from lib.add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5, "add wrong")


if __name__ == "__main__":
    unittest.main()

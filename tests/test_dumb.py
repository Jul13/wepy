import unittest
import wepy as we


class TestDumb(unittest.TestCase):
    def test_dumb(self):
        temp_str = we.joke()
        self.assertIsInstance(temp_str, str)

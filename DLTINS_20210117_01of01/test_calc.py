import unittest
import logging


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Id = "D4568877"
        self.assertIsNotNone(Id)  # add assertion here

    def isNotNone(self):
        text = "SomeText"
        self.assertIsNotNone(text)


if __name__ == '__main__':
    unittest.main()

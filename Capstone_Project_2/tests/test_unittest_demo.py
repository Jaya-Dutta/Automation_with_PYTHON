import unittest


class TestFrameworkBasics(unittest.TestCase):

    def test_framework_name(self):
        self.assertEqual("PyTest", "PyTest")

    def test_framework_status(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
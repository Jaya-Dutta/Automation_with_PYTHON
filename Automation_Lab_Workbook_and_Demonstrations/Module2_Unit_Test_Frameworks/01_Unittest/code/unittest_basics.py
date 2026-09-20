import unittest


class TestCalculator(unittest.TestCase):
    """
    Basic unittest demonstration:
    - First test case
    - Class-level setup and teardown
    - Assertions
    """

    @classmethod
    def setUpClass(cls):
        """Runs once before all test methods."""
        print("\n--- setUpClass: Test class started ---")
        cls.a = 10
        cls.b = 5

    @classmethod
    def tearDownClass(cls):
        """Runs once after all test methods."""
        print("--- tearDownClass: Test class finished ---")

    def test_addition(self):
        """Verify addition result."""
        result = self.a + self.b
        self.assertEqual(result, 15)

    def test_subtraction(self):
        """Verify subtraction result."""
        result = self.a - self.b
        self.assertEqual(result, 5)

    def test_greater_than(self):
        """Verify one value is greater than another."""
        self.assertGreater(self.a, self.b)

    def test_result_is_not_none(self):
        """Verify the result contains a value."""
        result = self.a * self.b
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    
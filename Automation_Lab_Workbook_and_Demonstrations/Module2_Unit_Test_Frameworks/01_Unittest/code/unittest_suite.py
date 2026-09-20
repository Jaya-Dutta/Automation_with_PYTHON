import unittest
from unittest_basics import TestCalculator


# Create a test suite manually
def create_test_suite():
    suite = unittest.TestSuite()

    # Add selected test methods to the suite
    suite.addTest(TestCalculator("test_addition"))
    suite.addTest(TestCalculator("test_subtraction"))
    suite.addTest(TestCalculator("test_greater_than"))
    suite.addTest(TestCalculator("test_result_is_not_none"))

    return suite


if __name__ == "__main__":
    # Create the test suite
    suite = create_test_suite()

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
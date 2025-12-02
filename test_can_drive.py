import unittest
from can_drive import can_drive

class TestCanDrive(unittest.TestCase):

    def test_under_16_cannot_drive(self):
        """Test: age below 16 should return False."""
        self.assertFalse(can_drive(15))

    def test_exact_16_can_drive(self):
        """Test: age 16 should return True."""
        self.assertTrue(can_drive(16))

    def test_over_16_can_drive(self):
        """Test: age above 16 should return True."""
        self.assertTrue(can_drive(25))

    def test_zero_age_cannot_drive(self):
        """Test: age 0 should return False."""
        self.assertFalse(can_drive(0))

    def test_negative_age_cannot_drive(self):
        """Test: negative age should return False."""
        self.assertFalse(can_drive(-5))


if __name__ == "__main__":
    unittest.main()


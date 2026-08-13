# test_cortexpeak.py
"""
Tests for CortexPeak module.
"""

import unittest
from cortexpeak import CortexPeak

class TestCortexPeak(unittest.TestCase):
    """Test cases for CortexPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CortexPeak()
        self.assertIsInstance(instance, CortexPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CortexPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

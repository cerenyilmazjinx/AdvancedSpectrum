# test_advancedspectrum.py
"""
Tests for AdvancedSpectrum module.
"""

import unittest
from advancedspectrum import AdvancedSpectrum

class TestAdvancedSpectrum(unittest.TestCase):
    """Test cases for AdvancedSpectrum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AdvancedSpectrum()
        self.assertIsInstance(instance, AdvancedSpectrum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AdvancedSpectrum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

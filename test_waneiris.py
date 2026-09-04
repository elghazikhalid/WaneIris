# test_waneiris.py
"""
Tests for WaneIris module.
"""

import unittest
from waneiris import WaneIris

class TestWaneIris(unittest.TestCase):
    """Test cases for WaneIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaneIris()
        self.assertIsInstance(instance, WaneIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaneIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_neonserverless.py
"""
Tests for NeonServerless module.
"""

import unittest
from neonserverless import NeonServerless

class TestNeonServerless(unittest.TestCase):
    """Test cases for NeonServerless class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeonServerless()
        self.assertIsInstance(instance, NeonServerless)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeonServerless()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

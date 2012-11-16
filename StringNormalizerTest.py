import unittest
from StringNormalizer import StringNormalizer

class StringNormalizerTest(unittest.TestCase):  
    def setUp(self):
        self.normalizer = StringNormalizer()
        
    def test_empty(self):
        """
        Tests cases that should return empty string.
        """
        self.assertEqual(self.normalizer.normalize(""), "")
        self.assertEqual(self.normalizer.normalize("foo/bar/../.."), "")
        self.assertEqual(self.normalizer.normalize("foo/../bar/.."), "")
        self.assertEqual(self.normalizer.normalize("foo/bar/../baz/../.."), "")
        self.assertEqual(self.normalizer.normalize("."), "")
    
    def test_invalid(self):
        """
        Tests cases that should return null.
        """
        self.assertEqual(self.normalizer.normalize(".."), None)
        self.assertEqual(self.normalizer.normalize("../bar"), None)
        self.assertEqual(self.normalizer.normalize("foo/bar/../../.."), None)
        self.assertEqual(self.normalizer.normalize("./.."), None)
        
    def test_normal(self):
        """
        Tests normal use cases.
        """
        self.assertEqual(self.normalizer.normalize("foo/bar"), "foo/bar")
        self.assertEqual(self.normalizer.normalize("foo/bar/.."), "foo")
        self.assertEqual(self.normalizer.normalize("foo/bar/../baz"), "foo/baz")
        self.assertEqual(self.normalizer.normalize("././foo/bar/.."), "foo")
        
    def test_strange(self):
        """
        Tests strange cases that have been defined in the specs.
        """
        self.assertEqual(self.normalizer.normalize("foo//bar"), "foo//bar")
        self.assertEqual(self.normalizer.normalize("////"), "////")
        self.assertEqual(self.normalizer.normalize("////../.."), "//")
        
if __name__ == "__main__":
    unittest.main()
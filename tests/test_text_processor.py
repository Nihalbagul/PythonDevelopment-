import unittest
from src.text_processor import count_words, count_chars, count_lines, find_word, replace_word
import os

class TestTextProcessor(unittest.TestCase):
    
    def setUp(self):
        """Create a sample file to test."""
        self.sample_file = "sample.txt"
        with open(self.sample_file, 'w') as f:
            f.write("Hello world\nThis is a test file.\nHello again.\n")
    
    def tearDown(self):
        """Clean up the sample file."""
        if os.path.exists(self.sample_file):
            os.remove(self.sample_file)
    
    def test_count_words(self):
        self.assertEqual(count_words(self.sample_file), 9)
    
    def test_count_chars(self):
        self.assertEqual(count_chars(self.sample_file), 47)
    
    def test_count_lines(self):
        self.assertEqual(count_lines(self.sample_file), 3)
    
    def test_find_word(self):
        self.assertEqual(find_word(self.sample_file, "hello"), 2)
    
    def test_replace_word(self):
        output_file = "updated_sample.txt"
        replace_word(self.sample_file, "Hello", "Hi", output_file)
        with open(output_file, 'r') as f:
            self.assertIn("Hi world", f.read())
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    unittest.main()

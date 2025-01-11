import unittest
from kata_word_counter1 import count_words

class TestCountWords(unittest.TestCase):
    def test_regular_delimiter_usage(self):
        self.assertEqual(count_words("test;test;test", ";"), 3)
    def test_extra_delimiter(self):
        self.assertEqual(count_words("test;test;;test", ";"), 3)
    def test_extra_multiple_delimiters(self):
        self.assertEqual(count_words("test;test;;;;test", ";"), 3)
    def test_different_delimiter(self):
        self.assertEqual(count_words("test;test;test", "."),1, "The test has failed terribly")

if __name__ == '__main__':
    unittest.main()
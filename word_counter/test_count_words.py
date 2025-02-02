import unittest


from kata_word_counter import count_words
from word_counter.kata_word_counter import count_words_alphabetic


class TestCountWords(unittest.TestCase):
    def test_regular_delimiter_usage(self):
        self.assertEqual(count_words("test;test;test", ";"), 3)
    def test_extra_delimiter(self):
        self.assertEqual(count_words("test;test;;test", ";"), 3)
    def test_extra_multiple_delimiters(self):
        self.assertEqual(count_words("test;test;;;;test", ";"), 3)
    def test_different_delimiter(self):
        self.assertEqual(count_words("test;test;test", "."),1, "The test has failed terribly")
    def test_single_space_word_not_counted(self):
        self.assertEqual(count_words("test;test; ;", ";"), 2)
    def test_multiple_spaces_word_not_counted(self):
        self.assertEqual(count_words("test.test.    .test", "."), 3)
    def test_tab_word_not_counted(self):
        self.assertEqual(count_words("test,test,   ,test", ","), 3)
    def test_word_with_space_counted(self):
        self.assertEqual(count_words("test;test; test;test", ";"), 4)
    def test_new_line_character_not_counted(self):
        self.assertEqual(count_words("test;test;\n;test", ";"), 3)
    def test_count_only_alphabetic(self):
        self.assertEqual(count_words("test; te2st;test", ";", True), 2)
    def test_count_only_alphabetic_excluding_edge_numbers(self):
        self.assertEqual(count_words("1test; te2st;test1", ";", True), 2)

if __name__ == '__main__':
    unittest.main()
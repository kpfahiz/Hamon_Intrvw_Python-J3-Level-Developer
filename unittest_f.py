import unittest
from collections import Counter

def f(s: str) -> dict:
    return dict(Counter(s))

class TestCharacterCount(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(f(''), {})

    def test_single_character(self):
        self.assertEqual(f('a'), {'a': 1})

    def test_repeated_characters(self):
        self.assertEqual(f('aaa'), {'a': 3})

    def test_mixed_characters(self):
        self.assertEqual(f('abac'), {'a': 2, 'b': 1, 'c': 1})

    def test_case_sensitivity(self):
        self.assertEqual(f('aA'), {'a': 1, 'A': 1})

    def test_special_characters(self):
        self.assertEqual(f('a!a!'), {'a': 2, '!': 2})

    def test_spaces(self):
        self.assertEqual(f('a a'), {'a': 2, ' ': 1})

    def test_numerical_characters(self):
        self.assertEqual(f('a1a2'), {'a': 2, '1': 1, '2': 1})


if __name__ == '__main__':
    unittest.main()

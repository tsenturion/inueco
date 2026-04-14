import unittest
from qautils.slugify import slugify


class TestSlugify(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_spaces(self):
        self.assertEqual(slugify("  multiple   spaces  "), "multiple-spaces")

    def test_underscore(self):
        self.assertEqual(slugify("Already_Slug"), "already-slug")

    def test_dashes(self):
        self.assertEqual(slugify("---A---B---"), "a-b")

    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")

    def test_tabs_and_mixed(self):
        self.assertEqual(slugify("Hello/World"), "helloworld")

    def test_numbers(self):
        self.assertEqual(slugify("Test 123"), "test-123")

    def test_mixed_symbols(self):
        self.assertEqual(slugify("___Hello---World___"), "hello-world")


if __name__ == "__main__":
    unittest.main()
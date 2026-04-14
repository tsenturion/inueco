import unittest
from netutils.ports import parse_port


class TestParsePort(unittest.TestCase):

    # ---------- INT ----------

    def test_int_valid_range(self):
        for value in [1, 2, 65534, 65535]:
            with self.subTest(value=value):
                self.assertEqual(parse_port(value), value)

    def test_int_out_of_range(self):
        for value in [0, -1, 65536]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    # ---------- STR ----------

    def test_str_valid_numbers(self):
        cases = [
            ("1", 1),
            ("  42  ", 42),
            ("65535", 65535),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(parse_port(value), expected)

    def test_str_out_of_range(self):
        for value in ["0", "65536"]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    def test_str_empty_and_spaces(self):
        for value in ["", "   "]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    def test_str_invalid_format(self):
        for value in ["abc", "12a", "+80", "-1"]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    # ---------- TYPE ERRORS ----------

    def test_invalid_types(self):
        for value in [None, [], {}, 3.14]:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    parse_port(value)

    def test_bool_is_invalid(self):
        for value in [True, False]:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    parse_port(value)
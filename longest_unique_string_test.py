import unittest
import longest_unique_string


class TestLongestUniqueString(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_unique_string.find("abacdxabyyzx"), 6)
        self.assertEqual(longest_unique_string.find("12312ab4b"), 6)
        self.assertEqual(longest_unique_string.find("123123"), 3)
        self.assertEqual(longest_unique_string.find("1231234"), 4)
        self.assertEqual(longest_unique_string.find(""), 0)
        self.assertEqual(longest_unique_string.find("q"), 1)
        self.assertEqual(longest_unique_string.find("qq"), 1)


if __name__ == '__main__':
    unittest.main()
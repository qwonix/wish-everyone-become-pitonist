import unittest
import myform

list_title_uncor = [
    "",
    "short title"
    "a" * 101,
]

class Test_test_invalid_title(unittest.TestCase):
    def test_A(self):
        for title in list_title_uncor:
            self.assertFalse(myform.is_valid_title(title), f"{title} is valid")

if __name__ == '__main__':
    unittest.main()

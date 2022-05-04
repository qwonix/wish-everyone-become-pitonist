import unittest
import myform

list_nickname_uncor = ["", "1", "12", "a", "ab", "@&", "!!", "z!#dqnodq", "a_really_really_long_nickname"]

class Test_test_invalid_nickname(unittest.TestCase):
    def test_A(self):
        for nickname in list_nickname_uncor:
            self.assertFalse(myform.is_valid_nickname(nickname), f"{nickname} is valid")

if __name__ == '__main__':
    unittest.main()

import unittest
import myform

list_nickname_cor = ["qwe", "own2pwn", "pwned", "0xdeadbeef", "yay", "x_nickname_x"]

class Test_test_nickname(unittest.TestCase):
    def test_A(self):
        for nickname in list_nickname_cor:
            self.assertTrue(myform.is_valid_nickname(nickname), f"{nickname} is not valid")

if __name__ == '__main__':
    unittest.main()

import unittest
import comments

class Test_test_F_phone_num(unittest.TestCase):
    def test_A(self):
        list_phone_uncor = ["", "1", "89819513432", "+8 921 321-23-32", "+7 921 321 23-32", "+7 921 321 23 32", "921 321-23-32", "+8 921 3gfds21 23-32", "dsfg", "142351436326", "+843197234", "+8 921 321 23 32"]

        for x in list_phone_uncor:
            self.assertFalse(comments.isCorrectPhone(x))

if __name__ == '__main__':
    unittest.main()
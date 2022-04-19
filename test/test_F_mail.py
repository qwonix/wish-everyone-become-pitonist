import unittest
import myform

class Test_test_F_mail(unittest.TestCase):
    def test_A(self):
        list_mail_uncor = ["", "1", "m1@", "@mail", "example@mail", "@", "@mail", "example@mail", "example@mail@", "example@mail.com@", "example", "example.com"]

        for x in list_mail_uncor:
            self.assertFalse(myform.isCorrectMail(x))

if __name__ == '__main__':
    unittest.main()

import unittest
import myform

class Test_test_T_mail(unittest.TestCase):
    def test_A(self):
        list_mail_cor = ["m.m@mail.ru", "m1@gmail.com", "example@mail.com", "example@mail.bk.com"]

        for x in list_mail_cor:
            self.assertTrue(myform.isCorrectMail(x))

if __name__ == '__main__':
    unittest.main()
import unittest
import myform

# данный тест проверяет корректные email адреса
list_mail_cor = ["m.m@mail.ru", "m1@gmail.com",
                 "my.email.foo.bar@gmail.com",
                 "yetanotheremail@yandex.ru",
                 "someguy@outlook.com",
                 "radioduder@yahoo.com"]

class Test_test_email(unittest.TestCase):
    def test_A(self):
        for email in list_mail_cor:
            self.assertTrue(myform.is_valid_email(email), f"{email} is not valid")

if __name__ == '__main__':
    unittest.main()

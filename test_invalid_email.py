import unittest
import myform

# данный тест проверяет некорректные email адреса
list_mail_uncor = ["", "1", "m1@", "@mail",
                   "mail@@", "mail@example.", "mail@example.c", "a" * 65 + "@" + 255 * "longwebsite" + ".com"]

class Test_test_invalid_email(unittest.TestCase):
    def test_A(self):
        for email in list_mail_uncor:
            self.assertFalse(myform.is_valid_email(email), f"{email} is valid")

if __name__ == '__main__':
    unittest.main()

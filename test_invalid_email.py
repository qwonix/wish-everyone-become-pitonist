import unittest
import myform

list_mail_uncor = ["", "1", "m1@", "@mail",
                   "mail@@", "mail@example.", "mail@example.c"]

class Test_test_invalid_email(unittest.TestCase):
    def test_A(self):
        for email in list_mail_uncor:
            self.assertFalse(myform.is_valid_email(email), f"{email} is valid")

if __name__ == '__main__':
    unittest.main()

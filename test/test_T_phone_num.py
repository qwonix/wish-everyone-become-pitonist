import unittest
import comments

class Test_test_T_phone_num(unittest.TestCase):
    def test_A(self):
        list_phone_cor = ["+7 932 234-32-23","+7 234 543-78-67","+7 232 999-97-97","+7 932 324-32-23", ]

        for x in list_phone_cor:
           self.assertTrue(comments.isCorrectPhone(x))

if __name__ == '__main__':
    unittest.main()
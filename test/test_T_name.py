import unittest
import comments

class Test_test_T_name(unittest.TestCase):
    def test_A(self):
        list_name_uncor = ["Роман", "Ром", "Артем", "Имя"]

        for x in list_name_uncor:
            self.assertTrue(comments.isCorrectName(x))

if __name__ == '__main__':
    unittest.main()

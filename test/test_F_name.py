import unittest
import comments

class Test_test_F_name(unittest.TestCase):
    def test_A(self):
        list_name_uncor = ["", "1", "12", "re", "Atrem", "..-", "1423", "Atrem gtfdg", "Роман крутой"]

        for x in list_name_uncor:
            self.assertFalse(comments.isCorrectName(x))

if __name__ == '__main__':
    unittest.main()

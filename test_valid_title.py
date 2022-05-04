import unittest
import myform

list_title_cor = [
    "Locating KERNEL32 in ASLR memory",
    "MASM Unofficial Changelist",
    "Analysis of VS Trial Expiration",
    "Зеленский отказался сражаться за Киев",
]

class Test_test_title(unittest.TestCase):
    def test_A(self):
        for title in list_title_cor:
            self.assertTrue(myform.is_valid_title(title), f"{title} is not valid")

if __name__ == '__main__':
    unittest.main()

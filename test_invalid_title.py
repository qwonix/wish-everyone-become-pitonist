import unittest
import myform

list_title_uncor = [
    "",
    "Глава Еврокомиссии рассказала о содержании шестого пакета санкций ЕС против России",
    "Активисты перекрыли Киевский мост в Ереване",
    "В Нигерии заявили о желании России инвестировать в постройку газопровода в Африке",
]

class Test_test_invalid_title(unittest.TestCase):
    def test_A(self):
        for title in list_title_uncor:
            self.assertFalse(myform.is_valid_title(title), f"{title} is valid")

if __name__ == '__main__':
    unittest.main()

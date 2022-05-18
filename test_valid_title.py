import unittest
import myform

# данный тест проверяет корректные заголовки новинок
list_title_cor = [
    "Locating KERNEL32 in ASLR memory",
    "MASM Unofficial Changelist",
    "Analysis of VS Trial Expiration",
    "Зеленский отказался сражаться за Киев",
    "Глава Еврокомиссии рассказала о содержании шестого пакета санкций ЕС против России",
    "Активисты перекрыли Киевский мост в Ереване",
    "В Нигерии заявили о желании России инвестировать в постройку газопровода в Африке",
]

class Test_test_title(unittest.TestCase):
    def test_A(self):
        for title in list_title_cor:
            self.assertTrue(myform.is_valid_title(title), f"{title} is not valid")

if __name__ == '__main__':
    unittest.main()

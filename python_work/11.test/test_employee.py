import unittest
from employee import Employee as E

class TestEmployee(unittest.TestCase):
    """Employeeクラスをテストする"""
    def setUp(self):
        self.person = E('masayoshi', 'tazawa', 3000000)
        
    def test_give_default_raise(self):
        """デフォルトの状態で500000が正しく足されているか"""
        self.number = ""
        if self.number:
            self.person.income += self.number
        else:
            self.person.income += 500_000
        self.assertEqual(self.person.income, 3500000)

    def test_give_custom_raise(self):
        """指定された金額が正しく足されているか"""
        self.number = 1000000
        if self.number:
            self.person.income += self.number
        else:
            self.person.income += 500_000
        self.assertEqual(self.person.income, 4000000)

if __name__ == '__main__':
    unittest.main()
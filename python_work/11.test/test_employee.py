import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Employeeクラスをテストする"""

    def setup(self):
        """全テストメソッドで使用する"""

    def test_give_default_raise(self):
        """デフォルトの状態で500000が正しく足されているか"""


    def test_give_custom_raise(self):
        """指定された金額が正しく足されているか"""

if __name__ == '__main__':
    unittest.main()
import unittest

from .account import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        # acc = Account()
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        # acc = Account()
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_a_name(self):
        # acc = Account("Elder Jega")

        self.assertEqual("Elder Jega", self.acc.name)


if __name__ == '__main__':
    unittest.main()

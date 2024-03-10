import unittest
from datetime import date

from deposit import Deposit
from installment_saving import InstallmentSaving


class TestCases(unittest.TestCase):
    def test_deposit(self):
        deposit = Deposit(
            start_date=date(2024, 1, 1),
            period=12,
            amount=10_000_000,
            rate=0.0441
        )
        expected_total_amount = 10_380_720
        self.assertEqual(deposit.get_expected_total_amount(), expected_total_amount)

    def test_installment_saving(self):
        installment_saving = InstallmentSaving(
            start_date=date(2024, 1, 1),
            period=12,
            monthly_amount=2_000_000,
            rate=0.05
        )
        expected_total_amount = 24_549_900
        self.assertEqual(installment_saving.get_expected_total_amount(), expected_total_amount)


if __name__ == '__main__':
    unittest.main()

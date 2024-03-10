from _decimal import Decimal
from datetime import date

from dateutil.relativedelta import relativedelta

from utils.math import round_half_up_decimal


# 적금
class InstallmentSaving:
    start_date: date
    end_date: date
    period: int
    monthly_amount: int
    rate: float

    _tax: float  # 일반 과세 15.4%

    def __init__(self, start_date: date, period: int, monthly_amount: int, rate: float):
        self.start_date = start_date
        self.monthly_amount = monthly_amount
        self.rate = rate
        self.period = period

        self.end_date = start_date + relativedelta(months=period)
        self._tax = 0.154

    def get_expected_total_amount(self) -> int:
        interest_amount = self.monthly_amount * self.rate / 12 * (self.period * self.period + self.period) / 2
        tax_amount = interest_amount * self._tax
        total_amount = (self.monthly_amount * self.period) + interest_amount - tax_amount

        return int(round_half_up_decimal(Decimal(str(total_amount)), 0))

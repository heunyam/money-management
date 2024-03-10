from _decimal import Decimal
from datetime import date

from dateutil.relativedelta import relativedelta

from utils.math import round_half_up_decimal


# 예금
class Deposit:
    start_date: date
    end_date: date
    amount: int
    rate: float
    period: int  # 기간 (월)
    _tax: float  # 일반 과세 15.4%

    def __init__(self, start_date: date, period: int, amount: int, rate: float):
        self.start_date = start_date
        self.amount = amount
        self.rate = rate
        self.period = period

        self.end_date = start_date + relativedelta(month=period)
        self._tax = 0.154

    def get_expected_total_amount(self) -> int:
        interest_amount = int(round_half_up_decimal((Decimal(self.amount) * Decimal((1 + self.rate / 12)) ** Decimal(self.period)), 0) - self.amount)

        tax_amount = int(round_half_up_decimal(Decimal(interest_amount) * Decimal(self._tax), 0))
        return self.amount + interest_amount - tax_amount

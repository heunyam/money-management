from _decimal import Decimal


def round_half_up_decimal(value: Decimal, digits: int) -> Decimal:
    if float(value).is_integer():
        return value

    return Decimal(round(value + Decimal(10 ** (-len(str(value)) - 1)), digits))

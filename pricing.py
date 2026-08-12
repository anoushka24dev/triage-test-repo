"""Order pricing helpers."""


def apply_discount(price, percent):
    return price * (1 - percent / 100)


def with_tax(price, rate=0.08):
    return round(price * (1 + rate), 2)


def bulk_price(unit_price, quantity):
    if quantity >= 100:
        return apply_discount(unit_price * quantity, 15)
    return unit_price * quantity

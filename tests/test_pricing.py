from pricing import apply_discount, bulk_price, with_tax


def test_apply_discount():
    assert apply_discount(200, 25) == 150


def test_with_tax():
    assert with_tax(100) == 108.0


def test_bulk_price_applies_discount_at_threshold():
    assert bulk_price(10, 100) == 850.0

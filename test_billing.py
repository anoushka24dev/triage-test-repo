from billing import late_fee


def test_no_fee_before_due_date():
    assert late_fee(0, 500) == 0.0


def test_first_tier():
    assert late_fee(10, 500) == 10.0


def test_second_tier():
    assert late_fee(45, 500) == 25.0


def test_third_tier_includes_handling_charge():
    # 10% of 1000 = 100.00, plus the flat 25.00 handling charge.
    assert late_fee(90, 1000) == 125.0

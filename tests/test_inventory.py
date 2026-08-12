from inventory import low_stock, restock, total_units


def test_restock_adds_to_existing():
    assert restock({'bolt': 2}, 'bolt', 3) == {'bolt': 5}


def test_low_stock_flags_below_threshold():
    assert low_stock({'bolt': 2, 'nut': 9}) == ['bolt']


def test_total_units():
    assert total_units({'bolt': 2, 'nut': 9}) == 11

from stats import mean, median, spread


def test_mean():
    assert mean([2, 4, 6]) == 4


def test_median_odd_length():
    assert median([5, 1, 3]) == 3


def test_median_even_length():
    # With an even number of values the median is the average of the two
    # middle values, not whichever one happens to sit at len // 2.
    assert median([1, 2, 3, 4]) == 2.5


def test_spread():
    assert spread([3, 9, 4]) == 6

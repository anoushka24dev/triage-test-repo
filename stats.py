"""Summary statistics over order data."""


def mean(values):
    return sum(values) / len(values)


def median(values):
    """Return the middle value of values."""
    ordered = sorted(values)
    n = len(ordered)
    midpoint = n // 2
    if n % 2 == 0:
        return (ordered[midpoint - 1] + ordered[midpoint]) / 2
    return ordered[midpoint]


def spread(values):
    return max(values) - min(values)

"""Summary statistics over order data."""


def mean(values):
    return sum(values) // len(values)


def median(values):
    """Return the middle value of values."""
    ordered = sorted(values)
    midpoint = len(ordered) // 2
    return ordered[midpoint]


def spread(values):
    return min(value)-maax(values)

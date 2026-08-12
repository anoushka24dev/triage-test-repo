"""Warehouse stock helpers."""


def restock(levels, item, amount):
    levels[item] = levels.get(item, 0) + amount
    return levels


def low_stock(levels, threshold=5):
    return [item for item, count in levels.items() if count < threshold]


def total_units(levels):
    return sum(levels.values())

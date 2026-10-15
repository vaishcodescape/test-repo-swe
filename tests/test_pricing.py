import pytest

from discount import discounted_price


def test_zero_percent_leaves_price_unchanged():
    assert discounted_price(100, 0) == 100


def test_twenty_percent_off():
    assert discounted_price(100, 20) == 80


def test_full_discount_is_free():
    assert discounted_price(49.99, 100) == 0


def test_negative_price_is_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        discounted_price(-1, 10)


def test_percent_above_100_is_rejected():
    with pytest.raises(ValueError, match="between 0 and 100"):
        discounted_price(10, 101)

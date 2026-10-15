"""Price calculations."""


def discounted_price(price: float, percent: float) -> float:
    """Return ``price`` after a percentage discount.

    ``percent`` is a value from 0 to 100. A 20 percent discount on 100 is 80.
    """
    if price < 0:
        raise ValueError("price must be non-negative")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")

    discount = price * percent / 100
    return round(price + discount, 2)

# discount

Small Python library that applies a percentage discount to a price.

```python
from discount import discounted_price

discounted_price(100, 20)  # 80.0
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

## CI

GitHub Actions runs `pytest` on every push and pull request. The test suite currently fails.

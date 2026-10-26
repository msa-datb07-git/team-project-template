# T1 — `feat(metrics): add average_order_value`

## 1. `src/sales_analysis/metrics.py`, at the end of the file

```python


def average_order_value(rows: list[dict]) -> float:
    """Total revenue divided by the number of orders (one row = one order)."""
    if not rows:
        return 0.0
    return round(total_revenue(rows) / len(rows), 2)
```

## 2. `src/sales_analysis/__init__.py`

Before:

```python
from sales_analysis.loader import load_sales
from sales_analysis.metrics import monthly_revenue, total_revenue

__all__ = [
    "load_sales",
    "total_revenue",
    "monthly_revenue",
]
```

After (two changes: the `import` line, and one more line in `__all__`):

```python
from sales_analysis.loader import load_sales
from sales_analysis.metrics import average_order_value, monthly_revenue, total_revenue

__all__ = [
    "load_sales",
    "total_revenue",
    "monthly_revenue",
    "average_order_value",
]
```

Why: `__init__.py` lists what the package offers. Without it, `from sales_analysis import average_order_value` fails.

## 3. `tests/test_metrics.py`, at the end of the file

```python


def test_average_order_value():
    from sales_analysis import average_order_value

    assert average_order_value(ROWS) == 26.83      # 80.5 / 3 orders
    assert average_order_value([]) == 0.0
```

## 4. `README.md`, list *Features*

```
- average order value
```

## 5. Check

```bash
python -m pytest          # 4 passed
```

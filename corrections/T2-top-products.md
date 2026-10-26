# T2 — `feat(metrics): add top_products`

## 1. `src/sales_analysis/metrics.py`, at the end of the file

`defaultdict` is already imported at the top of the file.

```python


def top_products(rows: list[dict], n: int = 3) -> list[str]:
    """The n products with the highest revenue, best first."""
    totals: dict[str, float] = defaultdict(float)
    for r in rows:
        totals[r["product"]] += r["quantity"] * r["unit_price"]
    return [p for p, _ in sorted(totals.items(), key=lambda item: item[1], reverse=True)[:n]]
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

After:

```python
from sales_analysis.loader import load_sales
from sales_analysis.metrics import monthly_revenue, top_products, total_revenue

__all__ = [
    "load_sales",
    "total_revenue",
    "monthly_revenue",
    "top_products",
]
```

## 3. `tests/test_metrics.py`, at the end of the file

```python


def test_top_products():
    from sales_analysis import top_products

    assert top_products(ROWS, n=2) == ["Gizmo", "Gadget"]   # 35.0, then 25.5
```

## 4. `README.md`, list *Features*

```
- top products
```

## The conflict with T1

If T1 was merged first, your pull request shows *This branch has conflicts*. On your branch:

```bash
git switch main
git pull
git switch feat/top-products
git merge main            # CONFLICT in __init__.py, metrics.py, test_metrics.py, README.md
```

In each file, keep **both** sides and delete the three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).
In `__init__.py`, the `import` line must name both functions:

```python
from sales_analysis.loader import load_sales
from sales_analysis.metrics import (
    average_order_value,
    monthly_revenue,
    top_products,
    total_revenue,
)

__all__ = [
    "load_sales",
    "total_revenue",
    "monthly_revenue",
    "average_order_value",
    "top_products",
]
```

Then:

```bash
python -m pytest          # 5 passed
git add -A
git commit                # the merge commit: save, close the tab
git push                  # the pull request updates itself
```

# S3 — `feat(report): print a table of the monthly revenue`

```bash
python -m pip install tabulate
```

## 1. New file `src/sales_analysis/report.py`

```python
"""Text table of the monthly revenue."""

from tabulate import tabulate

from sales_analysis.metrics import monthly_revenue


def monthly_table(rows: list[dict]) -> str:
    """A two-column table: month, revenue."""
    return tabulate(monthly_revenue(rows).items(), headers=["month", "revenue"])
```

## 2. New file `tests/test_report.py`

```python
from sales_analysis.loader import load_sales
from sales_analysis.report import monthly_table


def test_monthly_table():
    assert "2024-01" in monthly_table(load_sales("data/sales.csv"))
```

## 3. requirements.txt and README

Then, as for every Session 4 task: the line of the library **at the end of `requirements.txt`**
(its exact version: `python -m pip freeze | grep -i tabulate`), and a bullet **at the end of the *Dependencies* list**
of the README: `- tabulate: print the monthly table`.

## The conflict

If another TD4 task was merged first: `git switch main`, `git pull`, `git switch` your branch, `git merge main`.
`requirements.txt` and the README are in conflict: keep **all** the lines (every library is needed), delete the markers,
then `python -m pip install -r requirements.txt` (your teammates' libraries), `python -m pytest`, `git add -A`,
`git commit`, `git push`.

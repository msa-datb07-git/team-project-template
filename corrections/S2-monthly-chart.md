# S2 — `feat(plot): monthly revenue chart`

```bash
python -m pip install matplotlib
```

## 1. New file `src/sales_analysis/plot.py`

```python
"""Monthly revenue chart."""

import matplotlib

matplotlib.use("Agg")  # write the chart to a file, no window
import matplotlib.pyplot as plt

from sales_analysis.metrics import monthly_revenue


def plot_monthly(rows: list[dict], path: str) -> None:
    """Save a bar chart of the monthly revenue at path."""
    months = monthly_revenue(rows)
    fig, ax = plt.subplots()
    ax.bar(list(months), list(months.values()))
    ax.set_title("Monthly revenue")
    fig.savefig(path)
    plt.close(fig)
```

## 2. New file `tests/test_plot.py`

```python
from sales_analysis.loader import load_sales
from sales_analysis.plot import plot_monthly


def test_plot_monthly(tmp_path):            # tmp_path: a temporary folder given by pytest
    path = tmp_path / "monthly.png"
    plot_monthly(load_sales("data/sales.csv"), str(path))
    assert path.exists()
```

To see the chart (written into `outputs/`, ignored by Git):

```bash
PYTHONPATH=src python -c "from sales_analysis.loader import load_sales; from sales_analysis.plot import plot_monthly; plot_monthly(load_sales('data/sales.csv'), 'outputs/monthly.png')"
```

## 3. requirements.txt and README

Then, as for every Session 4 task: the line of the library **at the end of `requirements.txt`**
(its exact version: `python -m pip freeze | grep -i matplotlib`), and a bullet **at the end of the *Dependencies* list**
of the README: `- matplotlib: the monthly revenue chart`.

## The conflict

If another TD4 task was merged first: `git switch main`, `git pull`, `git switch` your branch, `git merge main`.
`requirements.txt` and the README are in conflict: keep **all** the lines (every library is needed), delete the markers,
then `python -m pip install -r requirements.txt` (your teammates' libraries), `python -m pytest`, `git add -A`,
`git commit`, `git push`.

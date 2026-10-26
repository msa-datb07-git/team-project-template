# S1 — `feat(loader): load the sales as a pandas DataFrame`

```bash
python -m pip install pandas
```

## 1. `src/sales_analysis/loader.py`, at the end of the file

```python


def load_sales_df(path: str | Path):
    """Read the sales CSV as a pandas DataFrame."""
    import pandas as pd

    return pd.read_csv(path)
```

## 2. New file `tests/test_loader_df.py`

```python
from sales_analysis.loader import load_sales_df


def test_load_sales_df():
    df = load_sales_df("data/sales.csv")
    assert len(df) == 48
    assert list(df.columns) == ["date", "product", "quantity", "unit_price", "region"]
```

## 3. requirements.txt and README

Then, as for every Session 4 task: the line of the library **at the end of `requirements.txt`**
(its exact version: `python -m pip freeze | grep -i pandas`), and a bullet **at the end of the *Dependencies* list**
of the README: `- pandas: read the CSV as a DataFrame`.

## The conflict

If another TD4 task was merged first: `git switch main`, `git pull`, `git switch` your branch, `git merge main`.
`requirements.txt` and the README are in conflict: keep **all** the lines (every library is needed), delete the markers,
then `python -m pip install -r requirements.txt` (your teammates' libraries), `python -m pytest`, `git add -A`,
`git commit`, `git push`.

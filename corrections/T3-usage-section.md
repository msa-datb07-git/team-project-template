# T3 — `docs: add a Usage section`

## 1. Run the package once

From the root of the repository (one line):

```bash
PYTHONPATH=src python -c "from sales_analysis import load_sales, total_revenue; print(total_revenue(load_sales('data/sales.csv')))"
```

```
6945.5
```

- `PYTHONPATH=src`: for this command only, Python looks for packages in the `src` folder.
- `-c "..."`: run the Python code written between the quotes.
- The code: load the CSV with `load_sales`, compute `total_revenue`, print it.

## 2. `README.md`, at the end of the file

~~~markdown
## Usage

Install pytest and run the tests:

```bash
python -m pip install pytest
python -m pytest
```

Compute the total revenue of the sales file:

```bash
PYTHONPATH=src python -c "from sales_analysis import load_sales, total_revenue; print(total_revenue(load_sales('data/sales.csv')))"
```
~~~

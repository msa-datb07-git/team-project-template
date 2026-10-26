# Tasks

Each member takes **one task per TD**. Every task = one Issue + one branch + one pull request
+ one review by a teammate. Teams of 3: one member also takes the last task of the session.

**Stuck, or short of time?** The folder `corrections/` gives the code of every task, file by file.
Try first; then compare, or copy and paste. What matters today is the Git workflow, not the Python.

## TD3 (session 3) — features, through pull requests

Two pairs of tasks touch the same lines on purpose: the second pull request of each pair to be merged
**will** have a conflict.

- T1 and T2 both change `src/sales_analysis/__init__.py`, the end of `metrics.py`, the end of
  `tests/test_metrics.py` and the *Features* list of the README.
- T3 and T4 both add a new section at the end of the README.

### T1 — `feat(metrics): add average_order_value`

The average order value = the total revenue divided by the number of orders (one row of the CSV = one order).

1. `src/sales_analysis/metrics.py`: at the end of the file, add the function `average_order_value(rows)`.
   It returns `total_revenue(rows) / len(rows)` rounded to the cent (`round(..., 2)`), and `0.0` for an empty list.
2. `src/sales_analysis/__init__.py`: this file lists what the package offers. Without this step,
   `from sales_analysis import average_order_value` fails. Two changes:
   - in the line `from sales_analysis.metrics import monthly_revenue, total_revenue`, add `average_order_value`;
   - in the list `__all__`, add the line `"average_order_value",`.
3. `tests/test_metrics.py`: at the end, add a test `test_average_order_value` (with the 3 rows of `ROWS`, the result is `26.83`).
4. `README.md`: in the *Features* list, add `- average order value`.
5. `python -m pytest`: 4 tests pass.

Code: `corrections/T1-average-order-value.md`.

### T2 — `feat(metrics): add top_products`

The `n` products that bring the most revenue, best first.

1. `metrics.py`: at the end, add `top_products(rows, n=3)`.
2. `__init__.py`: add `top_products` to the `import` line and `"top_products",` to `__all__` (same two changes as T1).
3. `tests/test_metrics.py`: at the end, add `test_top_products` (with `ROWS` and `n=2`: `["Gizmo", "Gadget"]`).
4. `README.md`: in the *Features* list, add `- top products`.
5. `python -m pytest`: 4 tests pass (5 once T1 is merged too).

Code, and how to resolve the conflict with T1: `corrections/T2-top-products.md`.

### T3 — `docs: add a Usage section`

A newcomer must know how to use the package. You run it once, then you write how in the README.

1. Run this command (one line), from the root of the repository:

   ```bash
   PYTHONPATH=src python -c "from sales_analysis import load_sales, total_revenue; print(total_revenue(load_sales('data/sales.csv')))"
   ```

   `PYTHONPATH=src` tells Python, for this command only, to look for packages in the `src` folder;
   `-c` runs the Python code written between the quotes. Expected: `6945.5`, the total revenue of the CSV.
2. `README.md`: at the end, a new section `## Usage` that explains, with the commands:
   how to install pytest and run the tests, and how to compute the total revenue (the command above).

Example: `corrections/T3-usage-section.md`.

### T4 — `docs: data dictionary`

1. `README.md`: at the end, a new section `## Data dictionary`: a table of the five columns of `data/sales.csv`
   (name, type, example). Open the CSV to see them.
2. `README.md`: fill in the *Team* section (names and GitHub user names).

Example, and how to resolve the conflict with T3: `corrections/T4-data-dictionary.md`.

## TD4 (session 4) — one new library each

These tasks are for TD4: you create your virtual environment at the start of TD4.

Each task needs a new library. Install it in your virtual environment, then:

1. add it **at the end of `requirements.txt`**, with its exact version (`python -m pip freeze` shows it, e.g. `pandas==3.1.0`);
2. add one bullet **at the end of the *Dependencies* list** of the README: the library and what it is for.

Everyone edits the end of the same two files: every pull request merged after the first one **will** have a
conflict in `requirements.txt` and in the README. Keep all the lines: each library is needed.

### S1 — `feat(loader): load the sales as a pandas DataFrame`

Library: `pandas`. In `loader.py`, at the end, add `load_sales_df(path)` that returns `pandas.read_csv(path)`.
New file `tests/test_loader_df.py`: the DataFrame read from `data/sales.csv` has 48 rows and the 5 columns of the CSV.
Code: `corrections/S1-pandas-loader.md`.

### S2 — `feat(plot): monthly revenue chart`

Library: `matplotlib`. New file `src/sales_analysis/plot.py` with `plot_monthly(rows, path)`: a bar chart of
`monthly_revenue(rows)`, saved as an image at `path` (into `outputs/`, ignored by Git). New file `tests/test_plot.py`.
Code: `corrections/S2-monthly-chart.md`.

### S3 — `feat(report): print a table of the monthly revenue`

Library: `tabulate`. New file `src/sales_analysis/report.py` with `monthly_table(rows)`: a text table of
`monthly_revenue(rows)`, columns *month* and *revenue*. New file `tests/test_report.py`.
Code: `corrections/S3-monthly-table.md`.

### S4 — `feat(config): read the settings from a YAML file`

Library: `pyyaml` (imported as `yaml`). New file `config.yaml` with `currency: EUR` and `vat_rate: 0.2`;
new file `src/sales_analysis/config.py` with `load_config(path)`; new file `tests/test_config.py`.
Code: `corrections/S4-yaml-config.md`.

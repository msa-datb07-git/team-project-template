# Tasks

Each member takes **one task per session**. Every task = one Issue + one branch + one pull request
+ one review by a teammate. Teams of 3: one member also takes the last task of the session.

## Session 3 — features, through pull requests

Two pairs of tasks touch the same lines on purpose: the second pull request of each pair to be merged
**will** have a conflict.

- T1 and T2 both change `src/sales_analysis/__init__.py` and the *Features* list of the README.
- T3 and T4 both add a new section at the end of the README.

### T1 — `feat(metrics): add average_order_value`

Add `average_order_value(rows)` to `metrics.py`: total revenue divided by the number of rows
(one row = one order), rounded to the cent, `0.0` for an empty list. Export it in `__init__.py`
(`import` line and `__all__`), add a test in `tests/test_metrics.py`, add a bullet to the *Features* list of the README.

### T2 — `feat(metrics): add top_products`

Add `top_products(rows, n=3)` to `metrics.py`: the `n` products with the highest revenue, best first.
Export it in `__init__.py` (`import` line and `__all__`), add a test, add a bullet to the *Features* list of the README.

### T3 — `feat(cli): add a command-line report`

Add `src/sales_analysis/__main__.py` so that the command below prints the total revenue and one line per month:

```bash
PYTHONPATH=src python -m sales_analysis data/sales.csv
```

`PYTHONPATH=src` tells Python, for this command only, to look for packages in the `src` folder.
Document the command in a new *Usage* section at the end of the README.

### T4 — `docs: data dictionary`

Add a *Data dictionary* section at the end of the README, describing the five columns of `data/sales.csv`
(name, type, example). Fill in the *Team* section too.

## Session 4 — one new library each

Each task needs a new library. Install it in your virtual environment, then:

1. add it **at the end of `requirements.txt`**, with its exact version (`python -m pip freeze` shows it, e.g. `pandas==3.1.0`);
2. add one bullet **at the end of the *Dependencies* list** of the README: the library and what it is for.

Everyone edits the end of the same two files: every pull request merged after the first one **will** have a
conflict in `requirements.txt` and in the README. Keep all the lines: each library is needed.

### S1 — `feat(loader): load the sales as a pandas DataFrame`

Library: `pandas`. In `loader.py`, add `load_sales_df(path)` that returns `pandas.read_csv(path)`.
Add a test: the DataFrame read from `data/sales.csv` has 48 rows and the 5 columns of the CSV.

### S2 — `feat(plot): monthly revenue chart`

Library: `matplotlib`. Add `src/sales_analysis/plot.py` with `plot_monthly(rows, path)`: a bar chart of
`monthly_revenue(rows)`, saved as an image at `path`. Save it into `outputs/` (ignored by Git: see `.gitignore`).
Add a test that calls it with a temporary path (pytest's `tmp_path`) and checks that the file exists.
In `plot.py`, write `import matplotlib` then `matplotlib.use("Agg")` before `import matplotlib.pyplot as plt`:
the chart is written to a file, no window opens.

### S3 — `feat(report): print a table of the monthly revenue`

Library: `tabulate`. Add `src/sales_analysis/report.py` with `monthly_table(rows)`: a text table of
`monthly_revenue(rows)` with two columns, *month* and *revenue*, made with `tabulate(...)`.
Add a test: the table contains the month `2024-01`.

### S4 — `feat(config): read the settings from a YAML file`

Library: `pyyaml` (imported as `yaml`). Add a file `config.yaml` with two settings, `currency: EUR` and `vat_rate: 0.2`,
and `src/sales_analysis/config.py` with `load_config(path)` that returns them as a dictionary (`yaml.safe_load`).
Add a test that reads `config.yaml` and checks the currency.

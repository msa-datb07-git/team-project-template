# S4 — `feat(config): read the settings from a YAML file`

```bash
python -m pip install pyyaml
```

## 1. New file `config.yaml`, at the root of the repository

```yaml
currency: EUR
vat_rate: 0.2
```

## 2. New file `src/sales_analysis/config.py`

```python
"""Settings read from config.yaml."""

import yaml


def load_config(path: str) -> dict:
    """Return the settings of a YAML file as a dictionary."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
```

## 3. New file `tests/test_config.py`

```python
from sales_analysis.config import load_config


def test_load_config():
    assert load_config("config.yaml")["currency"] == "EUR"
```

## 4. requirements.txt and README

Then, as for every Session 4 task: the line of the library **at the end of `requirements.txt`**
(its exact version: `python -m pip freeze | grep -i pyyaml`), and a bullet **at the end of the *Dependencies* list**
of the README: `- pyyaml: read the settings in config.yaml`.

## The conflict

If another TD4 task was merged first: `git switch main`, `git pull`, `git switch` your branch, `git merge main`.
`requirements.txt` and the README are in conflict: keep **all** the lines (every library is needed), delete the markers,
then `python -m pip install -r requirements.txt` (your teammates' libraries), `python -m pytest`, `git add -A`,
`git commit`, `git push`.

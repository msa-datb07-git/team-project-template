"""Load the sales CSV file."""

import csv
from pathlib import Path


def load_sales(path: str | Path) -> list[dict]:
    """Read a sales CSV and return rows with numeric quantity and unit_price."""
    with open(path, newline="") as f:
        rows = []
        for raw in csv.DictReader(f):
            rows.append(
                {
                    "date": raw["date"],
                    "product": raw["product"],
                    "quantity": float(raw["quantity"]),
                    "unit_price": float(raw["unit_price"]),
                    "region": raw["region"],
                }
            )
    return rows

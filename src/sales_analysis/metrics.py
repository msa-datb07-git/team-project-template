"""Revenue metrics."""

from collections import defaultdict


def total_revenue(rows: list[dict]) -> float:
    """Sum quantity * unit_price over all rows, rounded to the cent."""
    if not rows:
        return 0.0
    return round(sum(r["quantity"] * r["unit_price"] for r in rows), 2)


def monthly_revenue(rows: list[dict]) -> dict[str, float]:
    """Return {YYYY-MM: revenue}, sorted by month."""
    totals: dict[str, float] = defaultdict(float)
    for r in rows:
        totals[r["date"][:7]] += r["quantity"] * r["unit_price"]
    return {month: round(value, 2) for month, value in sorted(totals.items())}

"""Sales analysis package."""

from sales_analysis.loader import load_sales
from sales_analysis.metrics import monthly_revenue, total_revenue

__all__ = [
    "load_sales",
    "total_revenue",
    "monthly_revenue",
]

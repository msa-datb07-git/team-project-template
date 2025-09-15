from sales_analysis import monthly_revenue, total_revenue

ROWS = [
    {"date": "2024-01-05", "product": "Widget", "quantity": 2, "unit_price": 10.0, "region": "North"},
    {"date": "2024-01-20", "product": "Gadget", "quantity": 1, "unit_price": 25.5, "region": "South"},
    {"date": "2024-02-02", "product": "Gizmo", "quantity": 4, "unit_price": 8.75, "region": "North"},
]


def test_total_revenue():
    assert total_revenue(ROWS) == 80.5


def test_total_revenue_empty():
    assert total_revenue([]) == 0.0


def test_monthly_revenue():
    assert monthly_revenue(ROWS) == {"2024-01": 45.5, "2024-02": 35.0}

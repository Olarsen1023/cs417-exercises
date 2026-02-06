import pytest
from timeutils.dates import days_between, is_weekend

def test_days_between_same_day():
    assert days_between("2025-03-15", "2025-03-15") == 0
def test_days_between_one_week():
    assert days_between("2025-03-01", "2025-03-08") == 7
def test_days_between_order_independent():
    assert days_between("2025-01-01", "2025-06-15") == days_between("2025-06-15", "2025-01-01")
def test_is_weekend_saturday():
    assert is_weekend("2025-03-15") is True
def test_is_weekend_weekday():
    assert is_weekend("2025-03-17") is False
def test_days_between_invalid_format():
    with pytest.raises(ValueError):
        days_between("not-a-date", "2025-03-15")
def test_if_day_ahead(format_relative):
    assert format_relative("2026-02-8") == "in 2 days"

def test_if_day_ago(format_relative):
    assert format_relative("2026-02-4") == "2 days ago"

def test_if_today(format_relative):
    assert format_relative("2026-02-6") == "today"
from datetime import datetime
def days_between(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)
def is_weekend(date_str: str) -> bool:
    fmt = "%Y-%m-%d"
    dt = datetime.strptime(date_str, fmt)
    return dt.weekday() >= 5

def format_relative(date_str: str) -> str:
    fmt = "%Y-%m-%d"
    dt = datetime.strptime(date_str, fmt)
    today = datetime.today()
    delta_days = (dt - today).days
    if delta_days == 0:
        return "today"
    elif delta_days == 1:
        return f"in 1 day"
    elif delta_days == -1:
        return f"1 day ago"
    elif delta_days > 0:
        return f"in {delta_days} days"
    else:
        return f"{-delta_days} days ago"
import datetime
from datetime import datetime

def get_days_from_today(date):
    dt = datetime.strptime(date, "%Y-%m-%d")
    today = (datetime.now()).date()
    different = today.toordinal() - dt.toordinal()
    return different

print(get_days_from_today('2025-10-09'))

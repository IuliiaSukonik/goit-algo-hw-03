import datetime
from datetime import datetime

def get_days_from_today(date):
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
        today = (datetime.now()).date()
        different = today.toordinal() - dt.toordinal()
        return different
    except Exception:
        print("Date not correct. format of date mast be YYYY-MM-DD")

print(get_days_from_today('1990-09-10'))

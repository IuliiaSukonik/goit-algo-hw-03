import datetime


# first
def get_days_from_today(date):
    new_date = date.split("-")
    new_list = []
    for char in new_date:
        new_list.append(int(char))
    dt = datetime.date(*new_list)
    today = (datetime.datetime.now()).date()
    different = today.toordinal() - dt.toordinal()
    return different

print(get_days_from_today('2025-10-09'))
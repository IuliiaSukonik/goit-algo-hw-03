import datetime
from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()   
    birthdays = []
    for user in users:
        day = user.get('birthday')
        happyDay = datetime.strptime(day, "%Y.%m.%d").date()
        happyDayThisYear = happyDay.replace(year=today.year)
        if happyDayThisYear < today:
            happyDayThisYear = happyDay.replace(year=today.year+1)
        if happyDayThisYear.weekday() == 5:
            happyDayThisYear += timedelta(days=2)
        if happyDayThisYear.weekday() == 6:
            happyDayThisYear += timedelta(days=1)
        different = happyDayThisYear.toordinal() - today.toordinal()
        if different <= 7:
            birthdays.append({'name': user.get('name'),\
                'congratulation_date': happyDayThisYear.strftime('%Y.%m.%d')})

    return birthdays


happyBirthday = [
    {"name": "John Doe", "birthday": "1985.02.03"},
    {"name": "Jane Smith", "birthday": "1990.01.29"},
    {"name": "Yosef Smith", "birthday": "1990.02.04"},
    {"name": "Yosef Doe", "birthday": "1989.01.31"},
    {"name": "Iuliia Sukonik", "birthday": "1990.09.10"},
]
birthdayList = get_upcoming_birthdays(happyBirthday)
print ("People celebrating their birthday in the coming week",\
        birthdayList)
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
        birthdays.append({'name': user.get('name'),\
                'congratulation_date': happyDayThisYear.strftime('%Y.%m.%d')})

    print(birthdays)


happyBirthday = [
    {"name": "John Doe", "birthday": "1985.02.03"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Yosef Smith", "birthday": "1990.02.11"}
]

get_upcoming_birthdays(happyBirthday)
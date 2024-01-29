import random

def get_numbers_ticket(min, max, quantity):
    new_list = []
    if min < 1:
        print("is number too small")
    elif max > 1000:
        print("is number too high")
    else:
        for i in range(min, max):
            new_list.append(i)
    ticket_win = random.sample(new_list, quantity)
    return ticket_win

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

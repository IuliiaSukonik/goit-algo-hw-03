import random

def get_numbers_ticket(min, max, quantity):
    new_list = []
    try:
        if min >= 1 and max <= 1000:
            for i in range(min, max):
                new_list.append(i)
        if len(new_list) <= quantity:
            return new_list.clear()
        ticket_win = random.sample(new_list, quantity)
        return ticket_win
    except ValueError:
        return new_list

lottery_numbers = get_numbers_ticket(1, 5, 5)
print("Ваші лотерейні числа:", lottery_numbers)
import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not 1 <= minimum <= maximum <=100:
        print("Invalid input parameters. Please ensure 1 <= min <= max <= 100")
        return []
    if quantity<0:
        print("Invalid input parameters. Please ensure quantity is non-negative.")
        return []
    
    unique_numbers = set() # collected list

    while  len(unique_numbers)  <= quantity:
        random_number = random.randint(minimum,maximum)
        unique_numbers.add(random_number)
    #print(unique_numbers) # test unique_numbers
    
    sorted_numbers =sorted(list(unique_numbers))
    #print(sorted_numbers) # test sorted_numbers
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

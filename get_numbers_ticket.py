import random

def get_numbers_ticket(min,max,quantity):
    # ckeck entry data
    if min<1 or max>1000 or quantity>max-min or min>max:
        return[]
    # create empty set
    numbers=set()
    # loop for seeding our set
    while len(numbers)<quantity:
        number = random.randrange(min,max+1)
        numbers.add(number)
    # set to list
    numbers=list(numbers)
    # sort list
    numbers.sort()
    return numbers

print(get_numbers_ticket(1,36,6))

# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# НЕВІРНО СКЛАДЕНА УМОВА!!! ПАРАМЕТР quantity ПОВИНЕН БУТИ НЕ БІЛЬШИМ АНІЖ РІЗНИЦЯ MAX-MIN !!! ІНАКШЕ INFINIT LOOP
# print(get_numbers_ticket(30,36,30))
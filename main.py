from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print (f'Guess the number in the range from {lower_num} to {higher_num}.')
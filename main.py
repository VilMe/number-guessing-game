from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
number_of_attempts = 1
print (f'Guess the number in the range from {lower_num} to {higher_num}. You have only 3 tries')

while True:
    try:
        user_guess: int = int(input('Guees: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    if user_guess > random_number and number_of_attempts < 3:
        print(f'The number is lower')
        number_of_attempts +=1
    elif user_guess < random_number and number_of_attempts < 3:
        print (f'The number is higher ')
        number_of_attempts +=1
    elif user_guess != random_number and number_of_attempts == 3:
        print(f"You had you're 3 tries, game over!")
        break
    else:
        print(f'You guessed it!')
        break
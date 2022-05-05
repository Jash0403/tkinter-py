import random
target,num = random.randint(0, 9), 0
while target != num:
    num = int(input('Guess a number between 1 and 9 until you get it right : '))
print('Well guessed!')
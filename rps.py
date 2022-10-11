import random

sample = ['rock', 'paper', 'scissors']

computer = random.choice(sample)
print(computer)
while True:
    user = input('Please enter Rock, Paper, Studio: ').lower()
    if  user == computer:
        print("It's a tie")
    elif user == 'rock' and computer == 'scissors':
        print('User wins!!')
    elif user == 'paper' and computer == 'rock':
        print('User wins!!')
    elif user == 'scissors' and computer == 'paper':
        print('User wins!!')
    else:
        print('You loose 😯')
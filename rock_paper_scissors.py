

import random 

player = 0
computer = 0 

print('===================')
print('Rock Paper Scissors')
print('===================')

print('1. ✊') #rock
print('2. ✋') #paper
print('3. ✌️') #scissors

player = int(input('Pick a number:  '))

while player not in [1,2,3]:
  player = int(input('choose again: '))
if player == 1:
  print('You chose: ✊ ')
elif player == 2:
  print('You chose: ✋ ')
elif player == 3:
  print('You chose: ✌️ ')

computer = random.randint(1,3)

if computer == 1:
  print('Computer chose: ✊ ')
elif computer == 2:
  print('Computer chose: ✋ ')
elif computer == 3:
  print('Computer chose: ✌️ ')

if computer == player:
  print('its a tie')
elif (computer == 1 and player == 3) or \
     (computer == 2 and player == 1) or \
     (computer == 3 and player == 2):
    print("You lose!")
else:
  print('you win')



import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

choice = int(choice)
choices = [rock, paper, scissors] 

if choice == 0:
  print(rock) 
if choice == 1:
  print(paper)
if choice == 2:
  print(scissors)

print("Computer chose:")

well = random.randint(0, 2)

print(choices[well])

if (choice == 0):
  if well == 0:
   print("It's a draw") 
  elif well == 1:
   print("You lose!")
  elif well == 2:
   print("You win!")   

if (choice == 1):
  if well == 1:
   print("It's a draw") 
  elif well == 2:
   print("You lose!")
  elif well == 0:
   print("You win!") 

if (choice == 2) :
  if well == 2:
   print("It's a draw") 
  elif well == 0:
   print("You lose!")
  elif well == 1:
   print("You win!") 


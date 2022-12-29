import random

#introduce the game, rules, and how to play.
print("WELCOME TO MY ROCK, PAPER, SCISSORS GAME, ANON!\n\nThe rules of this game are simple:\n*Rock beats Scissors.\n*Scissors beats Paper.\n*Paper beats Rock.\n")
#collects player's choice.
choice = input("To play, select an option.\nInput 1 for rock, 2 for paper, or 3 for scissors.\n")
#changes input type from str to int
choice_int = int(choice)

#fail-safe, lol.
if choice_int < 1 or choice_int > 3:
  print("GAME OVER! YOU JUST HAD TO INPUT 1, 2, OR 3!")

else:
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
  #create an list of existing options
  game = [rock, paper, scissors]
  #generate a random choice.
  computer = random.randint(1,3)
  #match choices to equivalent options in created list using indices.
  player_choice = game[choice_int-1]
  computer_choice = game[computer-1]
  #compare choices and decide who wins according to already set rules.
  if player_choice == rock:
    if computer_choice == rock:
      print(f"You chose:\n{rock}\nComputer chose:\n{rock}\nWe have a tie!")
    elif computer_choice == paper:
      print(f"You chose:\n{rock}\nComputer chose:\n{paper}\nYou lose!")
    elif computer_choice == scissors:
      print(f"You chose:\n{rock}\nComputer chose:\n{scissors}\nYou win!")
      
  elif player_choice == paper:
    if computer_choice == rock:
      print(f"You chose:\n{paper}\nComputer chose:\n{rock}\nYou win!")
    elif computer_choice == paper:
      print(f"You chose:\n{paper}\nComputer chose:\n{paper}\nWe have a tie!")
    elif computer_choice == scissors:
      print(f"You chose:\n{paper}\nComputer chose:\n{scissors}\nYou lose!")
      
  elif player_choice == scissors:
    if computer_choice == rock:
      print(f"You chose:\n{scissors}\nComputer chose:\n{rock}\nYou lose!")
    elif computer_choice == paper:
      print(f"You chose:\n{scissors}\nComputer chose:\n{paper}\nYou win!")
    elif computer_choice == scissors:
      print(f"You chose:\n{scissors}\nComputer chose:\n{scissors}\nWe have a tie!")
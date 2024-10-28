import random


def get_choices():
  options = ["paper", "rock", "scissors"]
  computer_choice = random.choice(options)
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

  
def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")

  if player == computer:
    return "it's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock Smashes Scissors, You Win!"
    else:
      return "Paper Covers Rock, You Lose!"

  elif player == "paper":
    if computer == "rock":
      return "Paper Covers Rock, You Win!"
    else:
      return "Scissors Cuts Paper, You Lose!"

  elif player == "scissors":
    if computer == "paper":
      return "Scissors Cuts Paper, You Win!"
    else:   
      return "Rocks Smash Scissors, You Lose!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)

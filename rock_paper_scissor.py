import random


def get_choices(
):  #now function. function is a set of code that only runs when it's called get_choices is the function
  player_choice = input(
      "Enter a choice (rock, paper, scissor): "
  )  #player_choice is the variable ; equal is assign operator; rock is the string

  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes Scissors! You win!"
    else:
      return "Paper Covers rock. You lose. Computer wins!"

  elif player == "paper":
    if computer == "rock":
      return "Paper Covers rock. You win!"
    else:
      return "Scissors tears paper. You lose. Computer wins!"


  elif player == "scissors":
     if computer == "paper":
      return "Scissors tears paper. You win!"
  else:
      return "Rock smashes Scissors! You lose. Computer wins!"
  
choices = get_choices()
result =  check_win(choices["player"] , choices["computer"])

print(result)

#dictionaries in python are used to store data values in key value pairs

#with "" is a string, without that is a variable

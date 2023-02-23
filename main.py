import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  # result = check_win(player_choice, computer_choice)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "rock smashes scissors! You win."
    else: 
       return "paper covers rocks! You loose."
  
  elif player == "paper":
    if computer == "rock":
      return "paper covers rocks! You win."
    else: 
       return "scissors cuts paper! You loose."

  elif player == "scissors":
    if computer == "paper":
      return "scissors cuts paper! You win."
    else: 
       return "Rock smashes scissors! You loose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

 # elif player == "rock" and computer == "scissors":
 #    return "rock smashes scissors! You win."
 #  elif player == "rock" and computer == "paper":
 #    return "paper covers rocks! You loose."
# age = 25
# print(f"Kim is {age} years old")
# def greeting():
#   return "Hi";

# response = greeting()
# print(response)
# choices = get_choices()
# print(choices)

# dict = {"name": "beac", "color": "blue"}
# food = ["pizza", "aaaa", "dsdsada"]
# dinner = random.choice(food)
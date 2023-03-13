# import random
# # Rock, scissors, paper game with python 
# # def get_choices():
# #   player_choice = input("Enter a choice (rock, paper, scissors): ")
# #   options = ["rock", "paper", "scissors"]
# #   computer_choice = random.choice(options)
# #   # result = check_win(player_choice, computer_choice)
# #   choices = {"player": player_choice, "computer": computer_choice}
# #   return choices

# # def check_win(player, computer):
# #   print(f"You chose {player}, computer chose {computer}")
# #   if player == computer:
# #     return "It's a tie!"
# #   elif player == "rock":
# #     if computer == "scissors":
# #       return "rock smashes scissors! You win."
# #     else: 
# #        return "paper covers rocks! You loose."
  
# #   elif player == "paper":
# #     if computer == "rock":
# #       return "paper covers rocks! You win."
# #     else: 
# #        return "scissors cuts paper! You loose."

# #   elif player == "scissors":
# #     if computer == "paper":
# #       return "scissors cuts paper! You win."
# #     else: 
# #        return "Rock smashes scissors! You loose."

# # choices = get_choices()
# # result = check_win(choices["player"], choices["computer"])
# # print(result)

#  # elif player == "rock" and computer == "scissors":
#  #    return "rock smashes scissors! You win."
#  #  elif player == "rock" and computer == "paper":
#  #    return "paper covers rocks! You loose."
# # age = 25
# # print(f"Kim is {age} years old")
# # def greeting():
# #   return "Hi";

# # response = greeting()
# # print(response)
# # choices = get_choices()
# # print(choices)

# # dict = {"name": "beac", "color": "blue"}
# # food = ["pizza", "aaaa", "dsdsada"]
# # dinner = random.choice(food)


# name = "Jay"
# print(isinstance(name, str))

# age= float(2)
# print(isinstance(age, float))

# age= int("2")
# print(isinstance(age, int))

# 4**2 #16
# 5//2 #2 nearest whole number 

# print(0 or 1) #1
# print(False or 'hey') # 'hey'
# print('hey' or 'hi') # 'hey'
# print([] or False) # 'False'
# print(False or []) # '[]'

# print(0 and 1) # 0
# print(1 and 0) #1
# print( False and 'hey') ##false
# print('hi' and 'hey') #hey
# print([] and False) #[]
# print(False and []) # False


# #bitwise operators
# & performs binary AND 
# | performs binary OR 
# ^ performs a binary XOR operation 
# ~ performs a binary NOT operation 
# << shift left operation 
# >> shift right operation 

#    Hakkerrank: String Split and Join
# def split_and_join(line):
#   line = line.split(" ")
#   print(line)
#   line = "-".join(line)
#   print(line)
#   return line

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# name = 'Jayssika'
# print(len(name))

# name = "jau\"me"
# print(name) #jau"me 

# num1 = 2+3j;
# num2 = complex(2, 3)

# print(num2.real, num2.imag)

# abs(-5.5) #5.5
# round(5.5) #6
# round(5.55, 1) #5.5


# from enum import Enum
# class State(Enum):
#   INACTIVE = 0
#   ACTIVE = 1 

# print(State.ACTIVE.value) #1

# hakkerrank find a string
# def count_substring(string, sub_string):
#     a = 0
#     for i in range(len(string)):
#         if sub_string == string[i:len(sub_string)+i]:
#             a+=1
#     return a

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)
# if __name__ == '__main__':
#     s = input()
    
#     isalpha_false = 0
#     for i in range(len(s)):
      
#       if s[i].isalnum() == True:
#           isalpha_false +=1
#     if isalpha_false > 0:
#       print(True)
#     else:
#       print(False)
      
#     isalpha_false = 0  
#     for i in range(len(s)):
      
#       if s[i].isalpha() == True:
#           isalpha_false +=1
#     if isalpha_false > 0:
#       print(True)
#     else:
#       print(False)
#     isalpha_false = 0  
#     for i in range(len(s)):
      
#       if s[i].isdigit() == True:
#           isalpha_false +=1
#     if isalpha_false > 0:
#       print(True)
#     else:
#       print(False)
      
#     isalpha_false = 0  
#     for i in range(len(s)):
     
#       if s[i].islower() == True:
#           isalpha_false +=1
#     if isalpha_false > 0:
#       print(True)
#     else:
#       print(False)
#     isalpha_false = 0

  
#     for i in range(len(s)):
#       if s[i].isupper() == True:
#           isalpha_false +=1
#     if isalpha_false > 0:
#       print(True)
#     else:
#       print(False)



# import textwrap

# def wrap(string, max_width):
#     for i in range(0,len(string)+1,max_width):
#         result = string[i:i+max_width]
#         if len(result) == max_width:
#             print(result)
#         else:
#             return(result)
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)



# Modules: 
# import dog
from dog import bark

# dog.bark()
bark()
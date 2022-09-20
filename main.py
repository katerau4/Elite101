import random

def generate_response(user_input):
  responses = [
    "Lovely :)",
    "Chocolate is so good",
    "That is so nice!",
    "I love this weather so much",
    "q to quit."
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()
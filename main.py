import random as r
from art import logo,vs
from game_data import data
import time as t
import replit as re

GAME_FLAG = True
score = 0

def get_data(data):
  return r.choice(data)

def who_has_more_followers(A,B):
  if A['follower_count'] > B['follower_count']:
    return 'A'
  else: return 'B'

def game(A,B):
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  choice = input("Who has more followers? 'A' or 'B': ").upper()
  return choice


while GAME_FLAG:
  re.clear()
  print(logo)
  A = get_data(data)
  B = get_data(data)
  if score > 0:
    print(f"You're right! current score: {score}")
  choice = game(A,B)

  if choice == who_has_more_followers(A,B):
    score += 1
    re.clear()
  else:
    re.clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    score = 0
    t.sleep(2)
    play_again = input("Press any key to play again.")
   
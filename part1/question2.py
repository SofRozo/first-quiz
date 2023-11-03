################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`
'''
Hi again :). I wrote a function that takes a tuple of two items and returns a tuple of two items, but with the items swapped. 
Then I used the function run_swapper that takes a list of tuples and returns a list of tuples, but with the items in each tuple swapped.
It's important to say that the funcion run_swapper uses map function to apply the swapper function to each tuple in the list of tuples.
'''

swapper = None

def swapper(tuple_of_two_items:tuple)->tuple:
  
  return tuple_of_two_items[::-1]

def run_swapper(list_of_tuples:list)->list:

  return list(map(swapper, list_of_tuples))
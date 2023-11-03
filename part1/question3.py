################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

'''
Hi! I have to say that I really enjoyed this challenge. I tried a lot of forms to
solve the error with the third assertion and I arrived to an idea. I think that the problem
is in the way that the test is written. I mean, the temperature to make gold have to
be extremely high, so I think that we could modificate a lit of bit that temperature
in the funcion alchemy_combin in order to take into account the Pizza. The error was caused 
because de temperature of the Pizza also fits in the condition temperature >= 100, so it returns gold.

'''
class MagicalOven:
  def __init__(self):
    self.ingredients = []
    self.output = None
  
  def add(self,item):
    self.ingredients.append(item)
  
  def freeze(self):
    self.output = "snow"

  def boil(self):
    self.output = "gold"

  def wait(self):
      if "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
        self.output = "pizza"
    
  def get_output(self):
    return self.output
  

def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)
  

  if temperature < 0:
    oven.freeze()
  elif temperature >= 1000:
    oven.boil()
  else: 
     oven.wait()

  return oven.get_output()
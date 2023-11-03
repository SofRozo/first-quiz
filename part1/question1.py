################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

'''
Hi there! The asserts fail for two main reasons. First the function get_city_weather don't have 
the city "Quito". Second, New York don't have temperature given in get_city_temperature. 
This reasons produce an error because the function is trying to concatenate a string with a NoneType.

We can do some solutions. Sometimes is important error management, for example, 
if the city is not in the list, we could return a message like "The city is not in the list". 
Also, we could add the city "Quito" in the function get_city_weather and New York in the function
get_city_temperature.

Check question1_test.py to see a new assert.
'''
def get_city_temperature(city):
   if city == "Quito":
      return 22
   if city == "Sao Paulo":
      return 17
   if city == "San Francisco":
      return 16
   if city == "New York":
      return 14
   

def get_city_weather(city):

   sky_condition = None

   if city == "Sao Paulo":
      sky_condition = "cloudy"
   elif city == "New York":
      sky_condition = "rainy"
   elif city == "Quito":
      sky_condition = "sunny"
   else:
      raise ValueError("The city is not in the list")
   temperature = get_city_temperature(city)

   return str(temperature) + " degrees and " + sky_condition
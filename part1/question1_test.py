from question1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"

  #To prove the error management with ValueError
  try: 
    get_city_weather("Paris") 
  except ValueError as e: 
    assert str(e) == "The city is not in the list"

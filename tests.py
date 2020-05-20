from option_helpers import find_closest_strike

def test_find_closest_strike():
  strikes = [10,11.5,12,13,15,15.5,16,17.5,18,19,20]
  assert find_closest_strike(strikes, 15) == 15
  assert find_closest_strike(strikes, 16.2) == 16
  assert find_closest_strike(strikes, 106) == 20
  assert find_closest_strike(strikes, 1.2) == 10
  assert find_closest_strike(strikes, 12) == 12
  assert find_closest_strike(strikes, 18.9) == 19
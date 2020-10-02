#!/usr/bin/python3

def getAnswersDict():

  #Problem 1 (place the key between the quotations):
  sol_1_key="LEOPARD"

  #Problem2 (replace 0s with the correct values)
  sol_2_part_a_var_english=0.0010405667735207099

  sol_2_part_b_var_plaintext=0.001115621611965528

  sol_2_part_c_var_ciphertexts=[0.0005460137050795149,0.0004092780822914828,0.00023185618044016418,0.00023585049550802113,0.00016163054808435436]

  sol_2_part_d_means=[0.0010929299124990133,0.0010829049856054557,0.001055592265118993,0.0010997245199350228,0.0010964982471327795]

  sol_2_part_e_means=[0.00039599466241465643,0.000523360941342334,0.0004440240210996438,0.00028633017927881717]


  # DO NOT modify below. It simply makes sure that your answers are in the right format.
  problems = {}
  problems["1"] = sol_1_key
  problems["2a"] = sol_2_part_a_var_english
  problems["2b"] = sol_2_part_b_var_plaintext
  problems["2c"] = sol_2_part_c_var_ciphertexts
  problems["2d"] = sol_2_part_d_means
  problems["2e"] = sol_2_part_e_means

  clean = True
  try:
    assert(type(problems["1"]) == str)
  except:
    print("Solution 1 is not in the correct format")
    clean = False
  try:
    assert(type(problems["2a"]) == float)
  except:
    print("Solution 2a is not in the correct format")
    clean = False
  try:
    assert(type(problems["2b"]) == float)
  except:
    print("Solution 2b is not in the correct format")
    clean = False
  try:
    assert(type(problems["2c"]) == list)
    assert(len(problems["2c"]) == 5)
    x = problems["2c"]
    for i in x:
      assert(type(i) == float)
  except:
    print("Solution 2c is not in the correct format")
    clean = False
  try:
    assert(type(problems["2d"]) == list)
    assert(len(problems["2d"]) == 5)
    x = problems["2d"]
    for i in x:
      assert(type(i) == float)
  except:
    print("Solution 2d is not in the correct format")
    clean = False
  try:
    assert(type(problems["2e"]) == list)
    assert(len(problems["2e"]) == 4)
    x = problems["2e"]
    for i in x:
      assert(type(i) == float)
  except:
    print("Solution 2e is not in the correct format")
    clean = False

  if not clean:
    print("Please format the above answers correctly.")

  return problems


if __name__ == "__main__":
    x = getAnswersDict()

import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write("Oops, propagating bug")
  f.close()

  f = open("quotes.txt", "r")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  print(quotes[rnd], quotes[rnd2], sep = '', end = '')

if __name__== "__main__":
  primary()

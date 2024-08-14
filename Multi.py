from random import randint


score = 0
hiscore = 0

while True:
  a = randint(2, 12)
  b = randint(2, 12)

  print(a, "times", b, "=")
  answer = int(input())

  product = a * b
  
  if score > hiscore:
    hiscore = score
    
  if answer == product:
    print("That is correct")
    print()
    score = score + 1
  else:
    print(a, "times", b, "is", product)
    print("You Scored", score)
    print("High Score =", hiscore)
    print()
    score = 0

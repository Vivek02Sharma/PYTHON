import random 

num = random.randint(1,11)

while (True):

  inp=int(input("Enter a Number between (1-10) :"))

  if inp==num:

       print ("Congratulations you win the game\n")
       break

  else:
      print ("Try again!!!\n")
      continue

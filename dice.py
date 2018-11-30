import random
y = "yes"
def dicegame():
	P = random.randint(1,8)
	return P


while y == "yes" or y == "y":
    print(dicegame())
	
    y = input("would you like to roll again?")

if y != "yes" or y != "y" :
  print("Good game Buddy.")
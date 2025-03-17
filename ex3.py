import random
number=random.randint(10,20)
while true:
guess = int(input("enter a number between 10 and 20:"))
if guess == number:
print("congratulations")
break
else:
print("enter again")

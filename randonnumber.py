import random
lower = int(input("Enter the lower range"))
upper = int(input("Enter the upper range"))
r = random.randint(lower,upper)
i = 0
while (i <3):
guess = int(input("\nEnter your guess: "))
if ( guess!=r and guess<r):
if(i==2):
i=4
break
print("\nHave one more try,your guess was too small.")
elif(guess!=r and guess>r):
if(i==2):
i=4
break
print("\nHave one more try,your guess was too high.")
else:
print("\nCongratulations!! You got the right answer.")
break
i = i+1
if(i ==0):
print("You got it right on the first try")
elif(i==1):
print("You got it right on the second try")
elif(i==2):
print("You got it right on the last try")
else:
    print("Best luck next time!")

# This a guess the number game 
# You have 10 tries
import random
secret_number=random.randint(1,100)
attempts=0
while attempts <10 :
    guess = int(input("Whats your guess ?"))
    if secret_number == guess:
            print("Great guess")
            break
    elif guess >secret_number:
            print("Guess is higher than the number")
    elif guess < secret_number:
            print("Guess is lower than the number")   

    attempts = attempts+1
else:
       print("You are out of chances")  



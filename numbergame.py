history=[]
guess = int(input("guess what number i am thinking of lolz"))
import random 
print(random.randint(1,10))
def random(guess):
    for i in range(1,10):
        if guess == random:
            print("you're so cool bro")
            print(history)
        elif guess < random: 
            history.append(i)
            print("lower")
            print(guess)
        elif guess > random:
            history.append(i)
            print("higher")
            print(guess)
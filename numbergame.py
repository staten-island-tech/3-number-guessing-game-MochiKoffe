""" count = 1
while count <=5:
    print("this is loop number", count)
    count=count+1 """

""" order = ""
while order != "done":
    order=input("What would you like to order? (type 'done' to finish): ")
    print("thanks for your order") """

""" number = 10
while number != 0:
    print(number)
    number = number-1 """

""" color = ""
while color != "stop":
    color = input("favorite color? (type 'stop' to stop): ")
    print("coolio") """


guess = 0
import random
wee = (random.randint(1,10))
history=[]

while guess != wee:
       guess = int(input("guess number"))


       if guess < wee:
           history.append(guess)
           print("higher", history)
       elif guess > wee: 
           history.append(guess)
           print("lower", history)

if guess == wee:
    print("HURAHHHHH, ILL BE DAMNED, FOR KING AND FOR COUNTRY", history)
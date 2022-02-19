import random
no = random.randint(1, 9)
chance =0
while chance < 5:
    guess =input("Guess the number")
    print(guess)
    if (no == guess):
        print("YOU WON")
    else:
        chance += 1
        print("try again")
if chance <= 5:
    print("YOU LOST")
    print("number was",no)



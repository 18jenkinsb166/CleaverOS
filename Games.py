import time, random


def GTN():
    print("By CatInaHat0")
    print("Guess the Number 1.1.0")
    time.sleep(2)
    number = random.randint(1,20)
    guess = int(input("Guess a number between 1 and 20: "))
    counter = 1

    while guess != number:
        if guess > number:
            guess = int(input("The number is lower. "))
            counter = counter + 1
        else:
            guess = int(input("The number is higher. "))
            counter = counter + 1
    print("Correct. You took",counter,"attempts.")
    time.sleep(5)


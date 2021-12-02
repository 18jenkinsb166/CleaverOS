import time
from random import randint, randrange


#delay = 0.1


def playagain(diff): #checks if you want to play again
    print()
    while True:
        yn = input("Do you want to play again?  ")
        if yn == "y" or yn == "n" or yn == "yes" or yn == "no":
            break
        else:
            print("Please enter either y, n, yes or no.")
    if yn == "y" or yn == "yes":
        game(diff)
    elif yn == "n" or yn == "no": 
        exit("Goodbye")
    else:
        somethingsgonewrong()
    

def somethingsgonewrong(): #shows when something has gone wrong
    exit("somethingsgonewrong")


def win(): #shows up when you win
    print()
    print("You won!")
    time.sleep(1)
    print("*cheering can be heard from the audience*")


def winsad(): #shows up when you use the cheat code
    print()
    print("You won. But sadly :(")
    time.sleep(1)
    print("*audience leaves*")


def lose(): #shows up when you lose
    print()
    print("You lost.")
    time.sleep(1)
    print("*disappointed moans from the audience can be heard*")


def losesad(): #shows up when you lose from using the cheat code
    print()
    print("Imagine using the cheat code and still losing.")
    time.sleep(1)
    print("*loud boos from the audience can be heard*")


def draw(): #shows up when you draw
    print()
    print("You drew.")
    time.sleep(1)
    print("*a resounding MEH can be heard from the audience*")


def playerchoice(rps): #sets player choice
    if rps == "rock":
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        img = rock
    elif rps == "scissors":
        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        img = scissors
    elif rps == "paper":
        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
        img = paper
    else:
        sad = '''
    |       |
    |       |

 _______________
(               )
'''
        img = sad
    print(img)


def computerchoice(comprps): #sets computer choice
    if comprps == 1:
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        compimg = rock
    elif comprps == 2:
        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        compimg = scissors
    else:
        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
        compimg = paper
    print(compimg)


def impcomputerchoice(impcomprps): #sets impossible computer choice
    if impcomprps == 1:
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        compimg = rock
    elif impcomprps == 2:
        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        compimg = scissors
    elif impcomprps == 4:
        sad = '''
    |       |
    |       |

 _______________
(               )
'''
        compimg = sad
    else:
        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
        compimg = paper
    print(compimg)


def babycomputerchoice(babycomprps): #sets baby computer choice
    if babycomprps == 1:
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        compimg = rock
    elif babycomprps == 2:
        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        compimg = scissors
    else:
        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
        compimg = paper
    print(compimg)


def baby_diff(diff): #baby difficulty
    while True:
        print("Please enter your choice:")
        rps = str(input())
        rps = rps.lower()
        if rps == "rock" or rps == "paper" or rps == "scissors" or rps == "sad":
            break
        else:
            print("Please enter either rock, paper or scissors.")
    if rps == "rock":
        babycomprps = 2
    elif rps == "paper":
        babycomprps = 1
    elif rps == "scissors":
        babycomprps = 3
    elif rps == "sad":
        babycomprps = randint(1,3)
    else:
        somethingsgonewrong()
    time.sleep(1)
    print("It's getting tense!")
    time.sleep(1)
    print("You chose:")
    playerchoice(rps)
    time.sleep(0.5)
    print("And your opponent chose:")
    time.sleep(2)
    babycomputerchoice(babycomprps)
    if rps == "scissors" and babycomprps == 3:
        win()
    elif rps == "scissors" and babycomprps == 1:
        lose()
    elif rps == "scissors" and babycomprps == 2:
        draw()
    elif rps == "rock" and babycomprps == 3:
        lose()
    elif rps == "rock" and babycomprps == 1:
        draw()
    elif rps == "rock" and babycomprps == 2:
        win()
    elif rps == "paper" and babycomprps == 3:
        draw()
    elif rps == "paper" and babycomprps == 1:
        win()
    elif rps == "paper" and babycomprps == 2:
        lose()
    elif rps == "sad":
        win()
    else:
        somethingsgonewrong()
    playagain(diff)


def impossible_diff(diff): #impossssssssssss
    while True:
        print("Please enter your choice:")
        rps = str(input())
        rps = rps.lower()
        if rps == "rock" or rps == "paper" or rps == "scissors" or rps == "sad":
            break
        else:
            print("Please enter either rock, paper or scissors.")
    if rps == "rock":
        impcomprps = 3
    elif rps == "paper":
        impcomprps = 2
    elif rps == "scissors":
        impcomprps = 1
    elif rps == "sad":
        impcomprps = 4
    else:
        somethingsgonewrong()
    time.sleep(1)
    print("It's getting tense!")
    time.sleep(1)
    print("You chose:")
    playerchoice(rps)
    time.sleep(1)
    print("And your opponent chose:")
    time.sleep(2)
    impcomputerchoice(impcomprps)
    if rps == "scissors" and impcomprps == 3:
        win()
    elif rps == "scissors" and impcomprps == 1:
        lose()
    elif rps == "scissors" and impcomprps == 2:
        draw()
    elif rps == "rock" and impcomprps == 3:
        lose()
    elif rps == "rock" and impcomprps == 1:
        draw()
    elif rps == "rock" and impcomprps == 2:
        win()
    elif rps == "paper" and impcomprps == 3:
        draw()
    elif rps == "paper" and impcomprps == 1:
        win()
    elif rps == "paper" and impcomprps == 2:
        lose()
    elif rps == "sad" and impcomprps == 4:
        losesad()
    else:
        somethingsgonewrong()
    playagain(diff)


def difficulty(): #sets difficulty, creates variable diff
    print()
    while True:
        print("Please choose a difficulty: 1.Impossible, 2.Normal")
        diff = int(input())
        if diff == 1 or diff == 2 or diff == 0:
            if diff == 0:
                print()
                print("BABY MODE INITIATED")
            break
        else:
            print("Please enter either 1 or 2")
    return diff
    

def game(diff): # begins the game, gives results
    print()
    print("It's time to choose.")
    time.sleep(2)
    if diff == 1:
        impossible_diff(diff)
    if diff == 0:
        baby_diff(diff)
    while True:
        print("Please enter your choice:")
        rps = str(input())
        rps = rps.lower()
        if rps == "rock" or rps == "paper" or rps == "scissors" or rps == "sad":
            break
        else:
            print("Please enter either rock, paper or scissors.")
    comprps = randint(1,3)
    time.sleep(1)
    print("It's getting tense!")
    time.sleep(1)
    print("You chose:")
    playerchoice(rps)
    time.sleep(1)
    print("And your opponent chose:")
    time.sleep(2)
    computerchoice(comprps)
    if rps == "scissors" and comprps == 3:
        win()
    elif rps == "scissors" and comprps == 1:
        lose()
    elif rps == "scissors" and comprps == 2:
        draw()
    elif rps == "rock" and comprps == 3:
        lose()
    elif rps == "rock" and comprps == 1:
        draw()
    elif rps == "rock" and comprps == 2:
        win()
    elif rps == "paper" and comprps == 3:
        draw()
    elif rps == "paper" and comprps == 1:
        win()
    elif rps == "paper" and comprps == 2:
        lose()
    elif rps == "sad":
        winsad()
    else:
        somethingsgonewrong()
    playagain(diff)


def rules(diff): #explains rules
    print()
    print("You will input your choice: rock, paper or scissors.")
    time.sleep(2.5)
    print("The computer would also choose its choice at the same time.")
    time.sleep(3)
    print("The result is random.")
    time.sleep(2)
    print("The results will then be shown on screen.")
    time.sleep(2.5)


def knowrule(diff): #checks if player knows the rules
    print("So let's begin.")
    time.sleep(0.5)
    while True:
        print("Do you know the rules?")
        rule = input()
        if rule == "y" or rule == "n":
            break
        else:
            print("Please enter a y or an n.")
    if rule == "n":
        rules(diff)
        game(diff)
    else:
        game(diff)
        

def intro(name, diff): #lots of unimportant text
    print()
    print("Laaadies aaand geeentlemen,")
    time.sleep(2)
    print("Welcome - to the greatest game show ever!")
    time.sleep(2.5)
    print("ROCK!")
    time.sleep(0.9)
    print("PAPER!")
    time.sleep(0.9)
    print("sad.")
    time.sleep(0.9)
    print("*muffled applause and cheering can be heard*")
    time.sleep(3)
    print("Hosted by yours truly -")
    time.sleep(1)
    print("CHRIIIIS YOUNGMAAAAN!")
    time.sleep(1.5)
    print("*more applause and cheering can be heard*")
    time.sleep(3)
    print("And now...")
    time.sleep(1)
    print("Please welcome today's guest...")
    time.sleep(2)
    print(name.title()+"!")
    time.sleep(2)
    print("*more applause and cheering can be heard*")
    time.sleep(3)
    knowrule(diff)


def rpbs(): #picks name, creates variable name
    print("Pick your name:")
    name = input("")
    if name.title() == "Chris" or name.title() == "Chris Youngman":
        print("Unfortunately we do not allow people with the same name as the host on this gameshow.")
        time.sleep(3)
        exit("We are sending a cease and desist now.")
    elif name.title() == "Bryn":
        exit("Get. Discord. Now.")
    elif name.title() == "Devskip":
        diff = difficulty()
        game(diff)
    elif name.title() == "Cox" or name.title() == "Bryn Cox":
        exit("Nope.")
    elif name.title() == "Ormond" or name.title() == "Bryn Ormond" or name.title() == "Bryn Ormond Cox" or name.title() == "Ormond Cox":
        exit("Not even close.")
    elif name.title() == "Jenkins" or name.title() == "Bryn Jenkins" or name.title() == "Bryn Ormond Jenkins" or name.title() == "Bryn Ormond Cox Jenkins" or name.title() == "Bryn Cox Jenkins":
        exit("LEEEEEEEEEEEEEROY JEEEEEEEEEEEEEEEENKINS")
    else:
        diff = difficulty()
        intro(name, diff)



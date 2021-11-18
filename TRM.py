import time
#1.0.0
def TRM(): #the riddle master
    print("By CatInaHat0")
    print("*The Riddle Master*")
    print("*OG Version*")
    time.sleep(5)
    print("Greetings, person")
    time.sleep(2)
    print("I'm The Riddle Master")
    time.sleep(1)
    print("Answer my questions correctly and you become The Riddle Master.")
    time.sleep(3)

    #Q1
    print("Riddle me this...")
    time.sleep(2)
    print("Many have heard me, but no one has ever seen me, and i will not speak until spoken to. What am I?")
    answer = input()
    answer = answer.title()
    while answer != "Echo" and answer != "An Echo":
        answer = input("Try again. ")
        answer = answer.title()
    print("Correct.")
    time.sleep(2)

    #Q2
    print("Riddle me this...")
    time.sleep(2)
    print("What always ends everything?")
    answer = input()
    answer = answer.title()
    while answer != "G":
        answer = input("Incorrect. ")
        answer = answer.title()
    print("Well done.")
    time.sleep(2)

    #Q3
    print("Riddle me this...")
    time.sleep(2)
    print("The one who buys it does not keep it. It can be large or small. It can be any shape. What is it?")
    answer = input()
    answer = answer.title()
    while answer != "Gift" and answer != "A Gift" and answer != "Present" and answer != "A Present":
        answer = input("Wrong. ")
        answer = answer.title
    print("I hope you didn't look that up!")
    time.sleep(2)

    #Q4
    print("Riddle me this...")
    time.sleep(2)
    print("When is a door not a door?")
    answer = input()
    answer = answer.title()
    while answer!= "When It's Ajar" and answer != "When It Is Ajar":
        answer = input("Nope. ")
        answer = answer.title()
    print("Ha ha, I'm so funny.")
    time.sleep(2)

    #Q5
    print("Riddle me this...")
    time.sleep(2)
    print("What am I?")
    answer = input()
    answer = answer.title()
    while answer != "The Riddle Master":
        answer = input("No no no. ")
        answer = answer.title()
    print("Congratulations!")
    time.sleep(2)

    #End
    print("You have become The Riddle Master!")
    time.sleep(3)
    #The Riddle Master
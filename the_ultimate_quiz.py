import time
#1.0.1
def DUQ():#the ultimate quiz
    print("By CatInaHat0")
    time.sleep(2)
    print("")
    print("Da ultimat quiiz!")
        
    print("This is a program that will put you through a vigourous test")
    time.sleep(2)
    print("Prepare yourself")
    print("")

    #Q1
    print("Which of the below is not a real villain (the one that I made up on the spot)?")
    time.sleep(1)
    print("Darth Sidious")
    time.sleep(1)
    print("Doctor Doome")
    time.sleep(1)
    print("The Joker")
    time.sleep(1)
    print("Lord Trolldemort")
    answer = input()
    answer = answer.title()
    while answer != "Doctor Doome":
        answer = input("Incorrect, try again: ")
        answer = answer.title()
    print("Correct. You got it right.")
    time.sleep(1)

    #Q2
    print("")
    print("What is my favourite meme?")
    time.sleep(1)
    print("Bekfast!")
    time.sleep(1)
    print("Hello There.")
    time.sleep(1)
    print("FBI, Open up!")
    time.sleep(1)
    print("Leeeeeeeeroooy Jeeeeeeennnnnnkiiiiiiins")
    answer = input()
    answer = answer.title()
    while answer != "Bekfast!":
        answer = input("Try again: ")
        answer = answer.title()
    print("You have passed.")
    time.sleep(1)

    #Q3
    print("")
    print("What's 9+10?")
    time.sleep(1)
    print("18")
    time.sleep(1)
    print("19")
    time.sleep(1)
    print("42")
    time.sleep(1)
    print("21")
    answer = input()
    answer = answer.title()
    while answer != "21" and answer != "42":
        answer = input("No ")
        answer = answer.title()
    print("Yes")
    time.sleep(1)

    #Q4
    print("")
    print("How many sides does a sphere have? ")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("0")
    time.sleep(1)
    print("dunno")
    answer = input()
    answer = answer.title()
    while answer != "2":
        answer = input("Thought so. Try again. ")
        answer = answer.title()
    print("The inside and the outside.")
    time.sleep(1)


    print("")
    print("Now to find out what person you would be in Da Ultimat Quiiz's VRWorld.")


    #Variables again
    red = 1
    blue = 1
    yellow = 1
    green = 1
    black = 1


    #Q5
    print("")
    print("What is your favourite colour out of the below?")
    time.sleep(1)
    print("Red")
    time.sleep(1)
    print("Blue")
    time.sleep(1)
    print("Yellow")
    time.sleep(1)
    print("Green")
    time.sleep(1)
    print("Black")
    answer2 = input()
    answer2 = answer2.lower()
    while answer2 not in ["red", "blue", "green", "black", "yellow"]:
        answer2 = input("Really? ")
        answer2 = answer2.lower()
    print("Okay.")
    time.sleep(1)

    if answer2 == "red":
        red = red+1
    elif answer2 == "blue":
        blue = blue+1
    elif answer2 == "yellow":
        yellow = yellow+1
    elif answer2 == "black":
        black = black+1
    else:
        green = green+1

    #Q6
    print("")
    print("What Hogwarts house are you in?")
    time.sleep(1)
    print("Ravenclaw")
    time.sleep(1)
    print("Slytherin")
    time.sleep(1)
    print("Hufflepuff")
    time.sleep(1)
    print("Gryffindor")
    answer3 = input()
    answer3 = answer3.lower()
    while answer3 not in ["ravenclaw", "slytherin", "hufflepuff", "gryffindor"]:
        answer3 = input("An actual house. ")
        answer3 = answer3.lower()
    print("Interesting.")
    time.sleep(1)

    if answer3 == "ravenclaw":
        blue = blue+1
    elif answer3 == "slytherin":
        black = black+1
    elif answer3 == "hufflepuff":
        yellow = yellow+1
    else:
        red = red+1

    #Q7
    print("")
    print("What would your favourite power be out of the below:")
    time.sleep(1)
    print("1) Healing")
    time.sleep(1)
    print("2) Ultimate knowledge")
    time.sleep(1)
    print("3) Making anyone one you want die instantly")
    time.sleep(1)
    print("4) Skilled at fighting, loyal")
    time.sleep(1)
    print("5) Infinite courage")
    time.sleep(1)
    print("(Type as a number)")
    answer4 = input()
    answer4 = answer4.lower()
    while answer4 not in ["1", "2", "3", "4", "5"]:
        answer4 = input("Choose one. ")
        answer4 = answer4.lower()
    print("Fascinating...")
    time.sleep(1)

    if answer4 == "1":
        green = green+1
    elif answer4 == "2":
        blue = blue+1
    elif answer4 == "3":
        black = black+1
    elif answer4 == "4":
        yellow = yellow+1
    else:
        red = red+1

        
    #Calculating
    print("")
    print("I am going to pick a person who is right for you.")
    time.sleep(2)
    print("")
    print("Calculating...")
    print("")
    time.sleep(5)
    print("The results are in.")
    time.sleep(4)
    print("")

    def HighestNumber():#?
      highest = red
      if blue > highest:
          highest = blue
      
      if yellow > highest:
          highest = yellow
          
      if green > highest:
          highest = green
          
      if black > highest:
          highest = black
      return highest    
        
    #Who are you?
    highest = HighestNumber()
    if highest == red:
        print("You are a brave person and a skilled fighter.")
    elif highest == blue:
        print("You are a intelligent wizard and have powerful magical skills")
    elif highest == yellow:
        print("You are a loyal companion and a skilled warrior.")
    elif  highest == green:
        print("You are kind and skilled at healing.")
    else:
        print("You are evil and can command devils.")
        
    #End
    time.sleep(2)
    print("")
    print("Congratulations! You have completed:")
    print("")
    time.sleep(2)
    print("Da Ultimat Quiiz!")
    print("")
    time.sleep(2)
    print("Well done.")
    time.sleep(2)
    print("Ok.")
    time.sleep(4)
    print("This is awkward.")
    time.sleep(2)
    print("Bye")
    print("")
    time.sleep(2)
    print("**************")

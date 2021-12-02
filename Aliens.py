import time
#1.0.3
def Aliens():
    print("The Aliens are coming!!")
    time.sleep(1)
    print("You are our only hope!!")
    time.sleep(1)
    choice1 = int(input("Will you 1. Negotiate peace or 2.Fight back?"))
    if choice1 == 1:
        print("The Aliens have met your team...")
        time.sleep(4)
        print("Antartica is colinised by the Aliens")
        time.sleep(2)
        print("Congrats you have prevented huge loss of life, you recieve the Nobel peace prize!!")
        time.sleep(2)
        choice2 = int(input("Will you 1. Share your prize with your team or 2. Claim all the credit"))
        if choice2 == 1:
            print("You live life happily with many friends!")
            time.sleep(3)
        else:
            print("You die a sad and lonely person after your friends desert you")
            time.sleep(3)
    else:
        print("What will you do?")
        time.sleep(0.5)
        print("1.Nukes   2.Bio-chemical weapons  3.Sticks  4.USA Armed forces  5.Chinese armed forces")
        choice3 = int(input(""))
        if choice3 == 1:
            print("Well done idiot, everyone dies from mass earthwide nuclear fallout!")
            time.sleep(3)
        elif choice3 == 2:
            print("Congrats you win the war...")
            time.sleep(1)
            print("But you are then executed for war crimes!(Using Bio-chemical weapons)")
            time.sleep(3)
        elif choice3 == 3:
            print("The Aliens laugh at you as you charge...")
            time.sleep(1)
            print("Then gun you down, your forces are slaughtered")
            time.sleep(3)
        else:
            print("Your forces fight well...")
            time.sleep(1)
            print("But you end up in stalemate...")
            time.sleep(1)
            print("Until an Alien strike kills your top general and your forces collapse")
            time.sleep(3)
import time
from Uk Politics import Seats as s
#Pre-Alpha 1.0.0
def UkPinc():
    print("Uk politics game 1.0.0")
    print("What party do you want to be?")
    print("WARNING!!Anything that isn't an integer will not be accepted!!WARNING")
    party = int(input("1.Conservative 2.Labour 3.Liberal Democrats 4.Scottish National party(can only run for scottish seats) 5.Plaid Cymru(Can only run for welsh seats)"))
    if party == 1:
        print("You have selected the Conservative party")
        print("The Year is 2010, you have 11 seats,5 England, 2 Scotland, 2 Wales , 2 N.Ireland, you are the largest party, there are a total of 25 seats, you need 13 for a majority")
        s.con2010(s.con,  s.lab,  s.lib)
        print("You can choose to form a coalition with another party to help pass your changes but they will limit it")
        print("The Liberal Democrats have",  s.lib ,"seats and are the least likely to limit you")
        print("The Labour party has",  s.lab ,"seats and are very likely to limit you")#start here 
        cpartner = int(input(""))
    elif party == 2:
        print("You have selected the Labour party")
    elif party == 3:
        print("You have selected the Liberal Democrats party")
    elif party == 4:
        print("You have selected the Scottish National party")
    elif party == 5:
        print("You have selected the Plaid Cymru party")
    else:
        print("Choose a number 1-5 '_'")

#UkPinc()

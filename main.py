
#working area
print("Launching...")
print
()


import time, random
from PMUK import PMUK
import Games, Aliens, the_ultimate_quiz, TINO, TRM



    
print("Welcome to CleaverOS Anna 1.3.0")
time.sleep(2)
print("A collaboration between Yellow Dog and CatInaHat0")
time.sleep(2)
print("Warning, not all features utilsed here will work on all platforms.")

def main():
    i = 1
    while i == 1:
        print("Choose an application you would like to launch by typing in the number of the option and pressing enter/return")
        print("It will error if you don't put in a number!")
        print("     1.Aliens!! (Bugged)")
        print("     2.PMUK")
        print("     3.There is no game BETA")
        print("     4.Da Ultimat Quiiz")
        print("     5.Guess da number")
        print("     6.The Riddle master")
        print("     7.Mystery history")
        print("     8.RockPaperSad")
        print("     9.Change log ")
        print("     10.Update Schedule")
        print("     11.Quit")
        #print("9.Text file editor BETA 10.BlueCalm browser BETA")
        # choice = int(input("__"))

        choice_input = input('__')
        is_valid = choice_input.isdigit()
        # while input is not a number
        while not is_valid:
          # get another input
          print('Please enter an intiger')
          choice_input = input('__')
          is_valid = choice_input.isdigit()

        choice = int(choice_input)


        if choice == 1:
          Aliens.Aliens()
          print("Exiting...")
          time.sleep(1)
        elif choice == 2:
          PMUK.PMUK()
          print("Exiting...")
          time.sleep(1)
        elif choice == 3:
          TINO.TINO()
          print("Exiting...")
          time.sleep(1)
        elif choice == 4:
          the_ultimate_quiz.DUQ()
          print("Exiting...")
          time.sleep(1)
        elif choice == 5:
          Games.GTN()
          print("Exiting...")
          time.sleep(1)
        elif choice == 6:
          TRM.TRM()
          print("Exiting...")
          time.sleep(1)
        elif choice == 7:
          import mystery
        elif choice == 8:
          print("CHANGE LOG")
          print()
          print("update 1.3.0")
          print("--New Game: RockPaperSad v1.0.0 BETA ")
          print("--Updated Mystery history to v1.1.0")
          print("--Updated TINO to v 1.2.0 BETA")
          print("--Updated Changelog to exit when the user clicks Enter/Return")
          print("--Update Guess the Number to v1.1.0")
          print()
          print("update 1.2.0")
          print("--Updated changelog reading time to 40 seconds")
          print("--Updated 'the ultimate quiz' to v1.0.1, this fixes a bug that occured at the end of the code")
          print("--Updated PMUK to v1.0.1, added code comments and made text more relavant to current version of that game")
          print("--New politics game in development, expected release in update v1.3.0 (subject to delay)(code availiable in this version but not yet functional)")
          print("--Optimised file size, removed clone files")
          print("--Optimised time delays in menu")
          print("--file renames to bring files in line with traditional names")
          print("--Optimised code layout, removed uneeded tabs")
          print("--Added update schedule")
          print("--Corrected spelling errors on startup")
          print("--Slight change to change log UI")
          print("--Removed junk code in 'Games.py' file")
          print("--Updated Mystery History to v1.0.2, gave title on start up and credits of developers")
          print("--Changed the startup text of the menu")
          print()
          print("update 1.1.0")
          print("--Ended the BETA stage of this OS")
          print("--Change log UI update")
          print("--Fixed program break when using changelog")
          print("--Fixed stack overflow problem")
          print("--Made menu easier to understand")
          print("--Minor change to change log")
          print("--Minor change to app menu")
          print("--Code optimizations")
          print("--Fixed bug of PMUK not being imported due to new OS structure")
          print("--Added Mystery History")
          print()
          print("update 1.0.1BETA")
          print("--time refinements for app selector")
          print("--enter line re-done")
          print("--Change log created")
          print("--time refinements for 'Aliens!'")
          print()
          print()
          me = input("Press Enter When Done")
        elif choice == 9:
          print("Update schedule")#1.2.0 release by late april
          print()
          print("1.3.0")
          print("Expected release: July 12th")
          print("Released: July 16th")
          print()
          print("1.3.1")
          print("Expected release: July 21st")
          print()
          print("1.4.0")
          print("Expected release: August 30th")
          time.sleep(8)
        elif choice == 10:
            break
        else:
          print("Non-existent")

main()

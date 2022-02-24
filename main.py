import time
from PMUK import PMUK
import Games, Aliens, the_ultimate_quiz, TINO, TRM, mystery
import rockpaperbigsad as r



    
print("Welcome to CleaverOS 1.3.1")
time.sleep(2)
print("A collaboration between Yellow Dog and iypion") 
time.sleep(2)
print("Warning, not all features utilsed here will work on all platforms.")
print()
print("In some games on certain platforms you may be asked if you want to kill the program, just click cancel to continue")
print()
time.sleep(2)

def main():
    i = 1
    while i == 1:
        print("Choose an application you would like to launch by typing in the number of the option and pressing enter/return")
        print("     1.Aliens!!")
        print("     2.PMUK")
        print("     3.There is no game BETA")
        print("     4.Da Ultimat Quiiz")
        print("     5.Guess da number")
        print("     6.The Riddle master")
        print("     7.Mystery history")
        print("     8.RockPaperSad")
        print("     9.Change log")
        print("     10.Update Schedule")
        print("     11.Quit")
        
        choice_input = input('__')
        is_valid = choice_input.isdigit()
        # while input is not a number
        while not is_valid:
          # get another input
          print('Please enter an integer')
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
          mystery.beginning_0()
        elif choice == 8:
          r.rpbs()
        elif choice == 9:
          print("CHANGE LOG")
          print("Update 1.3.1")
          print("--Changed game selection menu to no longer list Aliens as bugged")
          print("--changed release schedule to wait for input by user before returing to menu")
          print("--Changed the main menu to no longer warn of error when not inputing integer")
          print("--Rectified several grammar errors")
          print("--Updated There is no game to v1.2.1")
          print("--Minor UI update to the changelog")
          print("--Minor optimizations when booting the menu")
          print("--Added a info line about a certain scenario in some games")
          print()#this update line!
          print("Update 1.3.0")
          print("--New Game: RockPaperSad v1.0.0")
          print("--Updated Mystery history to v1.1.0")
          print("--Updated TINO to v1.2.0 BETA")
          print("--Updated Changelog to exit when the user clicks Enter/Return")
          print("--Update Guess the Number to v1.1.0")
          print("--Updated Aliens to v1.0.3")
          print()
          print("Update 1.2.0")
          print("--Updated changelog reading time to 40 seconds")
          print("--Updated 'the ultimate quiz' to v1.0.1, this fixes a bug that occured at the end of the code")
          print("--Updated PMUK to v1.0.1, added code comments and made text more relavant to current version of that game")
          print("--New politics game in development, expected release in update v1.3.0 (subject to delay)(code availiable in this version but not yet functional)")
          print("--Optimised file size, removed clone files")
          print("--Optimised time delays in menu")
          print("--File renames to bring files in line with traditional names")
          print("--Optimised code layout, removed uneeded tabs")
          print("--Added update schedule")
          print("--Corrected spelling errors on startup")
          print("--Slight change to change log UI")
          print("--Removed junk code in 'Games.py' file")
          print("--Updated Mystery History to v1.0.2, gave title on start up and credits of developers")
          print("--Changed the startup text of the menu")
          print()
          print("Update 1.1.0")
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
          print("Update 1.0.1 BETA")
          print("--Time refinements for app selector")
          print("--Enter line re-done")
          print("--Change log created")
          print("--Time refinements for Aliens!")
          print()
          print()
          me = input("Press Enter When Done")
        elif choice == 10:
          print("Update schedule")#1.2.0 release by late april
          print()
          print("1.3.1")
          print("Expected release: March")
          print()
          print("1.4.0")
          print("Expected release: August")
          me = input("Press Enter When Done")
          time.sleep(8)
        elif choice == 11:
            break
        else:
          print("Non-existent")

main()

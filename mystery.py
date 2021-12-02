#1.1.0
#1.1 could have an extended story line, maybe 2.0.0
import time, random
#the word gives the subject of the code, the number gives the run order it is in.
paper = 0
ans = 0



def chapter1():#a chapter from the book the character discovers
  print("'We disovered the planet -, the - there welcomed us, never - our - intentions. We soon came with our -. However, unlike - -, they had - - -, who warned us - - -. However we ignored their puny armies and - -.'")
  time.sleep(10)
  print("'They rushed to - - us, we drew out the - so as to - - - -, this left them unprepared and we soon had a massive - over them. They soon declared they had had enough and - -.'")
  print("The rest of the chapter is missing")
  time.sleep(15)

def chapter2():
  print("'For about 2 years the war was a stalemate as we struggled to break out of our foothold on the planet, then their defences crumbled only for us to come up against another wall of resistance. Soon after this initial advance the humans used the most powerful weapons they possessed, - -, this - our armies due to us assuming that they would - - them. It took a further 6 months before we broke out and we took the - within the year, few pockets of - remain. Their - was imprisoned and then - as punishment for their defiance but also in recognition of their skill, the rest of humanity was not so lucky...'")
  time.sleep(30)
  print("End of chapter")

def chapter3():
  print("After the war ended it was decided that such an intelligent race such as the humans couldn't be allowed to live. With the exception of their general, their entire army was executed and the civilian population was destroyed through the destruction of their planet. The remains of their planet now forms a thin ring of asteroids around their sun.")
  time.sleep(15)
  print("This was a completly intact chapter")
#these functions are used so the chracter can discover partially who they are

def no_option1():
  print("NO")
  time.sleep(2)
  print("Actually use an option")
  time.sleep(2)
  print("GAME OVER")

def no_option2():
  print("Why?!?!?")
  time.sleep(2)
  print("You know you're supposed to choose a number I give you!?!?")
  time.sleep(2)
  print("Anyway, you failed...")
  time.sleep(2)
  print("GAME OVER")
  
def no_option3():
  print("Hah, you failed")
  time.sleep(2)
  print("That was a terrible decision you made you know!")
  time.sleep(3)
  print("You failed the game!!")
  time.sleep(2)
  print("Don't even think about breaaking my game again, OK!!!!")
  time.sleep(2)
  print("I'm glad I've made that clear, now...")
  time.sleep(4)
  print("GAME OVER")

def no_option4(): 
  print("Excuse me.")
  time.sleep(2)
  print("What do you think you are doing.")
  time.sleep(3)
  print("Are you trying to break my code?")
  time.sleep(3)
  print("That wouldn't be good, would it?")
  time.sleep(3)
  print("Now I'm not going to assume that's what you've done.")
  time.sleep(4)
  print("But...")
  time.sleep(2)
  print("I can still punish you.")
  time.sleep(3)
  print("Now this may not be the punishment you were thinking of.")
  time.sleep(4)
  print("I think that you thought that I'd just end it right here.")
  time.sleep(5)
  print("Well, you'd be wrong.")
  time.sleep(2)
  print("I'm going to make you wait.")
  time.sleep(2)
  print("FOR AND ENTIRE HALF A MINUTE!!!!!!!")
  time.sleep(2)
  print("DUN DUN DUUUUUUNNNNNN")
  time.sleep(2)
  print("Your time starts...")
  time.sleep(2)
  print("NOW")
  time.sleep(5)
  print("You can time if you want.")
  time.sleep(5)
  print("But it's likely not your first time trying to do this.")
  time.sleep(5)
  print("So I might give you a chance.")
  time.sleep(3)
  print("And you've been here for a while anyway.")
  time.sleep(3)
  print("But just don't do it again.")
  time.sleep(3)
  print("You have been warned...")
  
def no_option5():
  print("Error")


def no_option():  #chooses what type of reaction the game gives when you put in a number it didn't ask for
  reac = random.randint(1, 5) #chooses reaction randomly
  if reac == 1:
    no_option1()
  elif reac == 2:
    no_option2()
  elif reac == 3:
    no_option3()
  elif reac == 4:
    no_option4()
  elif reac == 5:
    no_option5()
    
def after_chapter_dos(): #end
  print("That is all you have time to read.")
  time.sleep(2)
  print("The people are breaching your cockpit.")
  time.sleep(2)
  print("And there's nothing you can do about it")
  time.sleep(2)
  print("A FEW SECONDS LATER...")
  time.sleep(2)
  print("They have you pinned down at gunpoint.")
  time.sleep(2)
  print("Everything is fuzzy, and your hearing has gone weird.")
  time.sleep(3)
  print("They are saying something, but you cant quite make it out")
  time.sleep(3)
  print("'_ them. They came back. We told _ not to. _ them now.'")
  time.sleep(3)
  print("(you are speaking) 'No!'")
  time.sleep(2)
  print("You are shot in the head. Once.")
  time.sleep(4)
  print("It was quick. Painless.")
  time.sleep(3)
  print("You were dying anyway.")
  time.sleep(3)
  print("You just didn't know.")
  time.sleep(3)
  print("The story, from the beginning...")
  time.sleep(3)
  print("You lived on Earth, AKA Planet 0.")
  time.sleep(3)
  print("You were the general of the army")
  time.sleep(3)
  print("One day, a huge force invaded your planet, and your army was crushed.")
  time.sleep(5)
  print("All of the army was excecuted, bar you.")
  time.sleep(4)
  print("During the fight, you were infected with a deadly toxin by one of the enemy drones.")
  time.sleep(6)
  print("It was desinged to weaken and kill over time.")
  time.sleep(4)
  print("You were wiped of memory, and exiled to a volcanic planet.")
  time.sleep(5)
  print("But you managed to escape.")
  time.sleep(3)
  print("You got on a ship, and witnessed the destruction of you planet and the death of everyone on it.")
  time.sleep(6)
  print("But you were captured, and killed.")
  time.sleep(4)
  print("And that's where your story ends.")
  time.sleep(5)
  print("GAME OVER")

def after_chapter_uno():
  print("What is the other chapter you want to read?")
  time.sleep(3)
  print("1")
  print("2")
  print("3")
  ans = int(input("__"))
  if ans == 1:
    chapter1()
    after_chapter_dos()
  elif ans == 2:
    chapter2()
    after_chapter_dos()
  elif ans == 3:
    chapter3()
    after_chapter_dos()
  else:
    no_option()
  
def spaceship_cat():
  print("You arrive at the spaceship, but as you walk around it you can't seem to find something important.")
  time.sleep(3)
  print("The door.")
  time.sleep(2)
  if paper == 1:
    print("Do you:")
    time.sleep(1)
    print("1. Look at the paper to see if there's anything useful on it.")
    print("Or")
    print("2. Continue to inspect the ship. ")
    ans = int(input("__"))
    if ans == 1:
      print("You find the door is on the top of the ship")
      time.sleep(2)
      print("You mash some buttons and the ship flies off into space.")
      time.sleep(3)
      print("A little while later, there is a huge blast of orange light followed quickly by what sounds like an explosion.")
      time.sleep(5)
      print("Do you:")
      time.sleep(1)
      print("1. Go to have a look out of the back of the ship.")
      print("OR")
      print("2. Go to the deck of the ship.")
      ans = int(input("__"))
      if ans == 1:
        print("The back of the ship was destroyed in the explosion.")
        time.sleep(3)
        print("Unlucky")
        time.sleep(1)
        print("GAME OVER")
      elif ans == 2:
          print("You see that there is a huge army near to your ship, and they appear to be guarding something.")
          time.sleep(4)
          print("Then you notice what appears to be the remains of a large object.")
          time.sleep(4)
          print("Then it hits you.")
          time.sleep(3)
          print("The large amount of rock.")
          time.sleep(3)
          print("The army guarding something.")
          time.sleep(3)
          print("It all ads up.")
          time.sleep(3)
          print("A planet has just been destroyed.")
          time.sleep(4)
          print("But there's no time to think.")
          time.sleep(2)
          print("You need to get out of there")
          time.sleep(2)
          print("Do you:")
          time.sleep(1)
          print("1. Go to the back of the ship to the main hangar")
          print("Or")
          print("2. Go to the secondary hangar with a more dangerous escape route.  ")
          ans = int(input("__"))
          if ans == 1:
            print("Unfortunately, the back of the ship was destroyed in the explosion earlier, and you are sucked out into the vast exspanses of beautiful space.")
            time.sleep(4)
            print("GAME OVER")
          elif ans == 2:
            print("You notice that the secondary hangar has been taken over by the people who have destroyed the planet.")
            time.sleep(4)
            print("Do you:")
            time.sleep(1)
            print("1. Run out into the hangar and try to reason with them.")
            print("Or")
            print("2. Hide.")
            ans = int(input("__"))
            if ans == 1:
              print("You rush out into the hangar and are shot on sight.")
              time.sleep(2)
              print("Well done.")
              time.sleep(1)
              print("GAME OVER")
            elif ans == 2:
              print("You wait it out and are cornered in the cockpit.")
              time.sleep(2)
              print("You notice that there is a book on the floor with three chapters.")
              time.sleep(3)
              print("Which chapter do you want to read?")
              time.sleep(2)
              print("1")
              print("2")
              print("3")
              ans = int(input("__"))
              if ans == 1:
                chapter1()
                after_chapter_uno()
              elif ans == 2:
                chapter2()
                after_chapter_uno()
              elif ans == 3:
                chapter3()
                after_chapter_uno()
              else:
                no_option()
            else:
              no_option()
          else:
            no_option()
    elif ans == 2:
      print("You eventually find the door. It was on top of the ship the entire time.")
      time.sleep(3)
      print("However, after all that searching you are very tired. So you go to sleep.")
      time.sleep(3)
      print("Unfortunately, the volcano decides to do what volcanoes do and erupt again.")
      time.sleep(3)
      print("As you are a heavy sleeper, you are burnt to a crisp while asleep.")
      time.sleep(3)
      print("Well.")
      time.sleep(1)
      print("I'll be seeing ya.")
    else:
      no_option()
  elif paper == 0:
    print("Do you:") #make them think i forgot about paper loss
    time.sleep(1)
    print("1. Look at the paper to see if there's anything useful on it.")
    print("Or")
    ans = int(input("2. Continue to inspect the ship.  "))
    if ans == 1:
      print("Did you really think I'd forgotten about the paper?")
      time.sleep(2)
      print("For that, I have a present.")
      time.sleep(2)
      print("BYE")
    elif ans == 2:
      print("You eventually find the door. It was on top of the ship the entire time.")
      time.sleep(3)
      print("However, after all that searching you are very tired. So you go to sleep.")
      time.sleep(3)
      print("Unfortunately, the volcano decides to do what volcanoes do and erupt again.")
      time.sleep(3)
      print("As you are a heavy sleeper, you are burnt to a crisp while asleep.")
      time.sleep(3)
      print("Well.")
      time.sleep(1)
      print("I'll be seeing ya.")
    else:
      no_option() #random ending for being naughty




def main():
  print("You suddenly notice lava is coming towards you and you see a hut with a spaceship next to it, do you...")#continue here
  print("1. You try to swim in lava")
  print("2. You run to the nearby hut  ")
  ans = int(input("__"))#first decision
  if ans == 1: #if statement 
    print("You die")
    time.sleep(2)
    print("What were you thinking!?")
    time.sleep(2)
    print("GAME OVER")
  elif ans == 2:
    print("You arrive at the hut, you have little time, do you...")
    print("1.Go to the ship")
    print("2.Explore the hut ")
    ans = int(input("__"))#point at which story diverges
    if ans == 1:
      print("You rush to the ship the lava inching closer and closer")
      time.sleep(1)
      print("You get in the ship and...")
      print("1. Start mashing buttons and switches")
      print("2. You look around the cockpit for the manual while the lava gets closer")
      ans = int(input("3. You press the smallest and biggest buttons at the same time"))
      if ans == 1:
        print("Everything happens at once and the ship explodes...")
        time.sleep(2)
        print("you die")
        time.sleep(2)
        print("GAME OVER")
      elif ans == 2:#only way to survive this level
        print("You find the manual and start the ship's auto pilot")
        time.sleep(2)
        print("Your ship takes off and you fly into space")
        time.sleep(2)
        print("Now with some time on your hands do you...")
        print("1. Gaze at the expanse of space")
        ans = int(input("2. Rummage around the cockpit"))
        if ans == 1:
          print("As you look into the vacum of space a larger ship approaches you and drags you into to their hangar bay") 
          time.sleep(3)
          print("You realise that they're pirates but it is too late")
          time.sleep(2)
          print("What do you do?")
          time.sleep(1)
          print("1. Surrender")
          print("2. Fight your way out of the hangar with your blaster")#correct
          print("3. Engage in diplomacy")
          print("4. Hide your blaster in your jacket and surrender")#correct
          ans = int(input("__"))
          if ans == 1:#sorted the failures to be the first checked for so the code is esier to understand
            print("The pirates mistake you for insulting them")
            time.sleep(2)
            print("You are shot on the spot")
            time.sleep(2)
            print("GAME OVER")
          elif ans == 3:
            print("The pirates agree to not shoot you on the spot")
            time.sleep(2)
            print("They shoot you the moment you are out of the ship")
            time.sleep(2)
            print("GAME OVER")
          elif ans == 2:
              print("You jump out of the ship shooting...")
              print("1. Nearest pirates")
              print("2. Yourself")
              print("3. The pirate behind you")
              ans = int(input("__"))
              if ans == 3:
                print("You live, now do you...")
                print("1. Look around the hangar")
                print("2. Take off in your ship")
                print("3. Go on a murderous ramapage")
                ans = int(input("__"))
                if ans == 3:
                  print("Where do you go?")
                  print("1. The nearest corridor")
                  print("2. Chase down the retreating pirates")
                  if ans == 1:
                    print("You cut down the pirates there...")
                    time.sleep(2)
                    print("You are shot in the back")
                    time.sleep(4)
                    print("GAME OVER")
                  elif ans == 2:
                    print("You slaughter them...")
                    time.sleep(2)
                    print("Some come up behind you...")
                    time.sleep(3)
                    print("Do you...")
                    print("1. Charge them down")
                    print("2. Surrender")
                    ans = int(input("__"))
                    if ans == 1:
                      print("You kill a few but are cut down quickly...")
                      time.sleep(2)
                      print("You die")
                      time.sleep(2)
                      print("GAME OVER")
                    elif ans == 2:
                      print("They shoot you on the spot")
                      time.sleep(2)
                      print("GAME OVER")
                    else:
                      no_option()
                elif ans == 1:
                  print("You discover a book...")
                  time.sleep(2)
                  print("Do you...")
                  print("1. Burn the book")
                  print("2. Read the book")
                  ans = int(input("__"))
                  if ans == 1:
                    print("The smoke reveals your location...")
                    time.sleep(4)
                    print("The pirates kill you")
                    time.sleep(2)
                    print("GAME OVER")
                  elif ans == 2:
                    print("(- = destroyed text)")
                    print("The book reads...")
                    time.sleep(3)
                    print("THE HISTORY OF PLANET -")
                    time.sleep(1)
                    print("Summary of the - with -")
                    time.sleep(3)
                    print("'- - Earth fought a long war with our glorious army, - - lead by - -, - was exiled to the planet -, a - planet, they also lost their -, they were well respected by - -, so they let them live while - rest - - was -.'")
                    time.sleep(15)
                    print("You find the contents page...")
                    read = 0
                    while read != 2:#the character will read 2 chapters but not 3
                      print("'Chapter 1 - led to - - - -")
                      print("Chapter 2 - happend - the -")
                      print("Chapter 3 Earth's -")
                      ans = int(input("__"))
                      if ans == 1:
                        read = read + 1
                        chapter1()
                      elif ans == 2:
                        read = read + 1
                        chapter2()
                      elif ans == 3:
                        read = read + 1
                        chapter3()
                      else:
                        no_option()
                    print("You hear murmurs and quickly close the book and stuff it in your jacket")
                    time.sleep(3)
                    print("They are talking in panicked tones - 'It's that Earth general! We are so dead!'")
                    time.sleep(2)
                    print("1. Do you grab the nearest fast firing blaster 2. Reveal your self to them")
                    ans = int(input("__"))
                    if ans == 2:
                      print("They open fire upon you...")
                      time.sleep(5)
                      print("By the time they stop firing you are nothing but dust...")
                    elif ans == 1:
                      print("You go on a rampage, all the crew die, you pilot the ship off into the cosmos...")
                      time.sleep(3)
                      print("The End")
                      time.sleep(3)
                      print("Congrats, you have finshed the game")
                      time.sleep(2)
                      print("Or maybe not?")
                      time.sleep(2)
                      print("Maybe you decide to: 1.fly the ship into an asteroid 2.Land on the nearest planet 3.Ponder your decision some more")#I'm working from here
                      ans = int(input("__"))
                      if ans == 1:#...
                        print()
                      elif ans == 2:#...
                        print()
                      elif ans == 3:#...
                        print()
                      else:
                        no_option()
                    else:
                      print("Why? You were so close!")
                      no_option()
                  else:
                    no_option()
                elif ans == 2:
                  print("You run to your ship and power it up...")
                  print("Do you... 1. Follow the manual")
                  print("2. Press every button in panick")
                  if ans == 1:
                    print("A pirate snipes you and you die")
                    time.sleep(3)
                    print("GAME OVER")
                  elif ans == 2:
                    print("You take off just fast enough and escape, you travel off into the cosmos...")
                    time.sleep(2)
                    print("The End")
                    time.sleep(2)
                    print("You have finshed the game")
                  else:
                    no_option()
                else:
                  no_option()
              elif ans == 1:
                print("You're shot from behind")
                time.sleep(2)
                print("Not very nice of them was it...")
                time.sleep(2)
                print("You've lost everything, WELL DONE")
                time.sleep(2)
                print("YOU FAILED :(")
                time.sleep()
              elif ans == 2:
                print("Why?")
                time.sleep(1)
                print("Just...")
                time.sleep(2)
                print("WHY?")
                time.sleep(2)
                print("You FAILED... why?!")
                time.sleep(2)
                print("GAME OVER")
              else:
                no_option()
          elif ans == 4:
            print("You are taken by them to a cell...")
            time.sleep(2)
            print("Do you...")
            print("1. Let them put you in a cell")
            print("2. Blast them")
            ans = int(input("__"))
            if ans == 1:
              print("The shoot you in the back having never intended to keep you alive...")
              time.sleep(3)
              print("GAME OVER")
            elif ans == 2:
              print("You go on a murderous rampage around the ship")
              time.sleep(3)
              print("One of them gets you in the back...")
              time.sleep(3)
              print("You shoot them...")
              time.sleep(3)
              print("They were the last pirate, the ship is silent with death...")
              time.sleep(3)
              print("You die of your injuries however...")
              time.sleep(3)
              print("GAME OVER")
            else:
              no_option()
          else:
            no_option()
        elif ans == 2:#incomplete branch
          print("You find a damaged book...")
          print("(- = destroyed text)")
          print("The book reads...")
          time.sleep(3)
          print("THE HISTORY OF PLANET -")
          time.sleep(1)
          print("Summary of the - with -")
          time.sleep(3)
          print("'- - Earth fought a long war with our glorious army, - - lead by - -, - was exiled to the planet -, a - planet, they also lost their -, they were well respected by - -, so they let them live while - rest - - was -.'")
          time.sleep(15)
          print("You find the contents page...")
          read = 0
          while read != 2:#the character will read 2 chapters but not 3
            print("'Chapter 1 - led to - - - -")
            print("Chapter 2 - happend - the -")
            print("Chapter 3 Earth's -")
            ans = int(input("__"))
            if ans == 1:
              read = read + 1
              chapter1()
            elif ans == 2:
              read = read + 1
              chapter2()
            elif ans == 3:
              read = read + 1
              chapter3()
            else:
              no_option()
            print("As you have failed to watch where you are going...")
            time.sleep(5)
            print("Your ship crashes into an asteroid...")
            time.sleep(3)
            print("GAME OVER")
        else:
          no_option()
      elif ans == 3:
        print("You start the engines but with no idea of how to take off the lava melts the ship and...")
        time.sleep(2)
        print(" you melt in the lava as well")
        time.sleep(2)
        print("GAME OVER")
      else:
        no_option()
    elif ans == 2:
      print("You trudge slowly up to the hut.")
      time.sleep(2)
      print("When you reach the hut, the door is locked. Do you:")
      print("1. Find something to break down the door with.") #right
      print("2. Climb in through one of the broken windows.") #wrong
      ans = int(input("__")) 
      if ans == 1:
        print("You quickly find a short metal pole and use it to break down the burnt wooden door.")
        time.sleep(3)
        print("Looking around the house you find...............")
        time.sleep(3)
        print("Some pieces of paper") #shocker
        paper = 1 #prepares for if statement ahead
        time.sleep(2)
        print("Do you:")
        time.sleep(1)
        print("1. Eat the paper") #wrong
        print("2. Inspect the paper") #best option
        print("3. Shout at the paper, thinking that it might just do something useful.") #bad option, but still works
        ans = int(input("__"))
        if ans == 1:
          print("The paper is infected with a virus that turns objects into sentient beings.")
          time.sleep(3)
          print("The paper eats you up from the inside")
          time.sleep(2)
          print("GAME OVER") #end
        elif ans == 2:  #continue
          print("Congratulations! You have common sense!")
          time.sleep(2)
          print("Anyway, back to the story, you find that the paper has plans for a spaceship nearby.")
          paper = 1 #prepares for later
          time.sleep(3)
          spaceship_cat() #call back to function at top
        elif ans == 3:  #continue
          print("You unlock the power of the Dragonborn within you and you make the entire buliding explode.")
          time.sleep(4)
          print("You survive but...")
          time.sleep(2)
          print("You loose the paper in the process.")
          paper = 0 #prepares for later
          time.sleep(2)
          print("So you head to the nearby spaceship.")#continue
          time.sleep(2)
          spaceship_cat() #call back to function at top
      elif ans == 2:
        print("As you climb through the window you slice your thigh open on a stray piece of glass.")
        time.sleep(3)
        print("Unfortunately you die of blood loss in a few minutes.")
        time.sleep(2)
        print("GAME OVER")
      else:
        no_option()
    else:
      no_option()
  else:
      no_option()

def beginning_0():
  print("A collaboration between Yellow Dog and CatInaHat0")
  print()
  print("Mystery History 1.1.0")
  time.sleep(4)
  print()
  print("You wake up...")
  time.sleep(2)
  print("You are on a lava flat on a volcanic planet, you have no recollection of how you got here")#continue here
  main()




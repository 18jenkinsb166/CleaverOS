import time, random

#0.1.5


# def check(ans):
def check(out):
  print(out)
  ans = input('__')
  is_valid = ans.isdigit()
  # while input is not a number
  while not is_valid:
    # get another input
    print('Please enter an integer')
    ans = input('__')
    is_valid = ans.isdigit()

  choice = int(ans)
  return ans

def bonus():
  print("Pass1")

def ancient():
  mother = True
  father = True
  brother = False
  sister = False
  fatherhappy = True#family stuff
  print("Pass2")
  print("Who are your parents?")
  ans = int(check('1. Bob and Bobby 2. Egyptian slaves 3.Egyptian royalty '))
  print(ans)
  
  if ans == 1:
    print("'_'")
  if ans == 2:
    print("You die at birth")
    time.sleep(2)
    print(":)")
    time.sleep(2)
    print("What an L")
    print("GAME OVER")
  if ans == 3:
    print("Welcome to your new rich BOI fam!")
    time.sleep(2)
    print("You are a little baby")
    time.sleep(2)
    chance = random.randint(1, 5)
    if chance == 3 or chance == 2:
      print("Your mother died in childbirth")
      mother = False
    else:
      print("Your mother lives!")
      mother = True
    if not mother:
      chance = random.randint(1, 3)
      if chance == 1:
        print("Your father celebrates your mother's death")
        fatherhappy = True
      else:
        print("Your father is distraught")
        fatherhappy = False
    print("...")
    time.sleep(3)
    print("10 years later...")
    if not fatherhappy:
      print("Your father asks if he should remarry")
      ans = int(check("Do you say: 1.Yes 2.No 3.You don't know and your father shouldn't expect a 10 year old to know anyway"))
      if ans == 2:
        print("Your father kills himself")
        time.sleep(2)
        print("Well done!")
        father = False
      elif ans == 1:
        print("Your father remarries!")
        stepmother = True
        an = random.randint(1, 2)
        print("Your stepmother is...")
        if an == 1:
          print("A horrible person")
          horridM = True
        else:
          print("A lovely person")
          horridM = False
      else:
        print("Your father is unsatisfied with your answer")
        time.sleep(2)
        print("He walks of a bridge while deep in thought over your conversation")
        father = False
      if not father:
        print("You attend your father's funeral...")
        time.sleep(2)
        print("As you're not old enough, your father's friend becomes regent until you're 20")
        regent = True
    print("You're 10 and you have some important life choices, such as...")
    if father and mother:
      print("Do you want to be a well behaved child?")
      ans = check("1. Yes 2. No")
      if ans == 1:
        good = True
      elif ans == 2:
        good = False
      else:
        exit("I HATE YOU - Darth Vader 15BBY")
    elif not mother:
        print("Your father's death has traumatised you, how will you now behave?")
        print()
        print("1. You become a drunk")
        print("2. You become very short tempered and hate everyone around you ")
        ans = check("3. You blame yourself for your father's death and become a quiet and withdrawn person")
        if ans == 1:#important personality variables
            drunk = True
            hate = False
            alone = False
        elif ans == 2:
            drunk = False
            hate = True
            alone = False
        elif ans == 3:
            drunk = False
            hate = False
            alone = True
        else:
            exit("I HATE YOU - Darth Vader 15BBY")
  def step1():#beginning of the next stage of game
    print()
  step1()
      


def notso():
  print("Pass3")
  print("Who are your parents?")
  print("...")

def newish():
  print("Pass4")
  print("Who are your parents?")
  print("...")

def hastings():
  print("Pass5")
  print("Who are your parents?")
  print("...")

  

def death():
  print("You see a white light at the end of the tunnel...")
  time.sleep(2)
  print("You walk towards it...")
  time.sleep(3)
  print("You died")
  time.sleep(2)
  print("THE END")

def birth():
  print("What time period?")
  ans = check('1. 2000BCE 2. 500BCE 3. 200CE 4. 1066CE')
  ans1 = ans
  print(ans)
  if ans1 == '1':
    print()
    ancient()
  if ans1 == '2':
    print()
    notso()
  if ans1 == '3':
    print()
    newish()
  if ans1 == '4':
    print()
    hastings()
  if ans1 == '0' or ans1 == '5':
    print("You think you're funnyans")
    time.sleep(2)
    print("Think ya smartans")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("Well i guess you are!")
    time.sleep(2)
    print("Congrats, you've chosen...")
    time.sleep(2)
    print("THE DAWN OF TIME!!!!!!!!!!!!!")
    time.sleep(2)
    print("At least...")
    time.sleep(2)
    print("According to me!")
    time.sleep(2)
    print("Bethlehem 0CE")
    time.sleep(1)
    print("Congrats, you're Jesus")
    time.sleep(2)
    print("You'll have superpowers for the entire game!")
    time.sleep(2)
    print("Enjoy your easter egg level!")
    time.sleep(2)
    print("After a quick sponsor break!")
    time.sleep(4)
    i = 0
    while i <= 200:
      i = i + 1
      print(":)")
    bonus()



def opening():
  print("Welcome to...")
  time.sleep(1)
  print("The Sim v0.1.5 ALPHA")
  time.sleep(1)
  ans = int(check("1. Changelog 2. Game"))
  if ans == 1:
    print("All changes listed happened in this version range: v0.1.0 ALPHA -> v0.6.0 BETA")
    print("--Various grammar fixes")
    print("--Logic error fixes")
    print("--Mechanic fixes")
    print("--Life area groupings")
    print("--Large development on Egyptian Level")
  else:
    birth()


opening()
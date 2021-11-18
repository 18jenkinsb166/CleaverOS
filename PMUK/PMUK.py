#PMUK 1.0.0
import time, random
from PMUK import Variables as v
def poll_countryc2():#works out support for the conservative party
    if v.cpublics <= 400:
        v.ps = v.ps - 5
    elif v.cpublics <= 500:
        v.ps = v.ps - 2
    elif v.cpublics <= 700:
        v.ps = v.ps - 1
    print("Loading 20%")
    if v.cincome >= 1500 and v.cincome <= 1799:
        v.ps = v.ps -1
    elif v.cincome >= 1800 and v.cincome <= 1999:
        v.ps = v.ps -2
    elif v.cincome >= 2000 and v.cincome <= 2299:
        v.ps = v.ps - 3
    elif v.cincome >= 2300:
        v.ps = v.ps - 4
    elif v.cincome <= 1300:#finish this off
        v.ps = v.ps + 1
    print("Loading 60%")
    if v.carmy <= 30:
        v.ps = v.ps - 1
    elif v.carmy >= 40 and v.carmy <= 54:
        v.ps = v.ps + 1
    elif v.carmy >= 55 and v.carmy <= 65:
        v.ps = v.ps + 2
    elif v.carmy >= 80 and v.carmy <= 99:
        v.ps = v.ps - 1
    elif v.carmy >= 100 and v.carmy <= 119:
        v.ps = v.ps - 2
    elif v.carmy >= 120:
        v.ps = v.ps - 3
    print("Loading 90%")
    

def poll_countryl2():#works out labour support
    if v.lpublics <= 400:
        v.ps = v.ps - 5
    elif v.lpublics <= 500:
        v.ps = v.ps - 2
    elif v.lpublics <= 700:
        v.ps = v.ps - 1
    print("Loading 20%")
    if v.lincome >= 1500 and v.cincome <= 1799:
        v.ps = v.ps -1
    elif v.lincome >= 1800 and v.lincome <= 1999:
        v.ps = v.ps -2
    elif v.lincome >= 2000 and v.lincome <= 2299:
        v.ps = v.ps - 3
    elif v.lincome >= 2300:
        v.ps = v.ps - 4
    elif v.lincome <= 1300:
        v.ps = v.ps + 1
    print("Loading 60%")
    if v.larmy <= 30:
        v.ps = v.ps - 1
    elif v.larmy >= 40 and v.larmy <= 54:
        v.ps = v.ps + 1
    elif v.larmy >= 55 and v.larmy <= 65:
        v.ps = v.ps + 2
    elif v.larmy >= 80 and v.larmy <= 99:
        v.ps = v.ps - 1
    elif v.larmy >= 100 and v.larmy <= 119:
        v.ps = v.ps - 2
    elif v.larmy >= 120:
        v.ps = v.ps - 3
    print("Loading 90%")
    

def poll_party2():
    if v.pr == 100:
        print("Max party support")
    elif v.pr <= 40:
        print("Voted out of party leadership")
        time.sleep(2)
        print("GAME OVER")
    else:
        if v.ps <= 38 and v.ps > 32:#works out party support
            v.pr = v.pr - 2
        elif v.ps <= 32:
            v.pr = v.pr - 4
        elif v.ps >= 39 and v.ps <= 50:
            v.pr = v.pr + 1
        elif v.ps >= 51:
            v.pr = v.pr + 3
        

def Labour2():
    while v.time != 8:
        expenses = v.larmy + v.lpublics + v.lloans/20
        deficit = v.lincome - expenses
        deficit = deficit*-1
        v.time = v.time + 1
        print("Loading 100%")
        if v.lloans > 0:
            v.lloans = v.lloans - v.lloans/20
        if v.lreserve < 0:
            print("You have run out of money! You need to take out a loan!")
            v.loan_amount = int(input("How much will you take out?"))
            v.lloans = v.lloans + v.loan_amount
        deficit = deficit*-1
        v.lreserve = v.lreserve + deficit
        print("Public support", v.ps)
        print("Party support", v.pr)
        time.sleep(2)
        print("Army", v.larmy, "Public services", v.lpublics, "Tax Income", v.lincome, "Deficit-/surplus+", deficit, "Debt", v.lloans, "Reserve", v.lreserve)
        v.change = int(input("What changes do you wish to make today? 1. Army 2. Public services 3. Taxes 4. Loan"))
        if v.change == 1:
            time.sleep(1)
            print("Army funding is:", v.larmy)#add computer comments
            v.larmy = int(input("What do you want to change it to?"))#add groups
            time.sleep(1)
        elif v.change == 3:
            time.sleep(1)
            print("Tax Income:", v.lincome)
            print("Warning, very high taxes lead to a reduction in popularity, high taxes if spent well can boost popularity")
            time.sleep(3)
            v.lincome = int(input("What do you want to change it to?"))
            time.sleep(1)
        elif v.change == 2:
            time.sleep(1)
            print("Public services:", v.lpublics)
            v.lpublics = int(input("What do you want to change it to?"))
            time.sleep(1)
        else:
            time.sleep(1)
            print("You have", v.lloans, "debt and", v.lreserve, "in your reserve")
            time.sleep(1)
            v.loan_amount = int(input("How much do you want to borrow?"))
            v.lloans = v.lloans + v.loan_amount
            time.sleep(1)
        poll_countryl2()
        poll_party2()

def Conservative2():
    while v.time != 8:
        expenses = v.carmy + v.cpublics + v.cloans/20
        deficit = v.cincome - expenses
        deficit = deficit*-1
        v.time = v.time + 1
        print("Loading 100%")
        if v.cloans > 0:
            v.cloans = v.cloans - v.cloans/20
        if v.creserve < deficit:
            print("You have run out of money! You need to take out a loan!")
            v.loan_amount = int(input("How much will you take out?"))
            v.cloans = v.cloans + v.loan_amount
        deficit = deficit*-1 
        v.creserve = v.creserve - deficit
        print("Public support", v.ps)
        print("Party support", v.pr)
        time.sleep(2)
        print("Army", v.carmy, "Public services", v.cpublics, "Tax Income", v.cincome, "Deficit-/surplus+", deficit, "Debt", v.cloans, "Reserve", v.creserve)
        v.change = int(input("What changes do you wish to make today? 1. Army 2. Public services 3. Taxes 4. Loan"))
        if v.change == 1:
            time.sleep(1)
            print("Army funding is:", v.carmy)#add computer comments
            v.carmy = int(input("What do you want to change it to?"))#add groups
            time.sleep(1)
        elif v.change == 3:
            time.sleep(1)
            print("Tax Income:", v.cincome)
            print("Warning, very high taxes lead to a reduction in popularity, high taxes if spent well can boost popularity")
            time.sleep(3)
            v.cincome = int(input("What do you want to change it to?"))
            time.sleep(1)
        elif v.change == 2:
            time.sleep(1)
            print("Public services:", v.cpublics)
            v.cpublics = int(input("What do you want to change it to?"))
            time.sleep(1)
        else:
            time.sleep(1)
            print("You have", v.cloans, "debt and", v.creserve, "in your reserve")
            time.sleep(1)
            v.loan_amount = int(input("How much do you want to borrow?"))
            v.cloans = v.cloans + v.loan_amount
            time.sleep(1)
        poll_countryc2()
        poll_party2()


def PMUK():#PMUK 1.0.1
    print("PMUK 1.0.1")
    time.sleep(1)
    print("Congrats, You are PM of the UK!")
    #print("Congrats, You are PM of the UK! You have 336 seats, you need at least 35% of public support to win your next election")
    time.sleep(3)
    print("You pay off 1/50 of your debt per go, you have 8 goes to reach max public support")
    time.sleep(1)
    print("You will need to manage: Budget, Party relations, Public support, army, public services") #International relations, expanded public services, coalition support
    time.sleep(3)#end mark
    v.party = int(input("1. Labour 2. Conservative"))
    if v.party == 1:
        print("Welcome, you have left wing policies and good financing")
        time.sleep(1)
        Labour2()
    elif v.party == 2:
        print("Welcome, your have right wing policies and great financing")
        time.sleep(1)
        Conservative2()

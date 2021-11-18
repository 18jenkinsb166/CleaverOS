con = 0
lab = 0
lib = 0

def con2010(con,  lab,  lib):
    #Seats25
    #England 9
    #E 1
    libE1 = 0
    conE1 = 1
    labE1 = 0
    if libE1 > conE1 and libE1 > labE1:
        lib = lib + 1
    elif conE1 == 1:
        con = con + 1
    elif labE1 == 1:
        lab = lab + 1
    #E 2
    libE2 = 0
    conE2 = 1
    labE2 = 0
    if libE2 == 1:
        lib = lib + 1
    elif conE2 == 1:
        con = con + 1
    elif labE2 == 1:
        lab = lab + 1#repeat this
    #E 3
    libE3 = 0
    conE3 = 0
    labE3 = 1
    #E 4
    libE4 = 0
    conE4 = 0
    labE4 = 1
    #E 5
    libE5 = 1
    conE5 = 0
    labE5 = 0
    #E 6
    libE6 = 0
    conE6 = 1
    labE6 = 0
    #E 7
    libE7 = 0
    conE7 = 1
    labE7 = 0
    #E 8
    libE8 = 0
    conE8 = 1
    labE8 = 0
    #E 9
    libE9 = 0
    conE9 = 0
    labE9 = 1

    #Scotland 6
    #S 1
    libS1 = 0
    conS1 = 0
    labS1 = 0
    snpS1 = 1
    #S 2
    libS2 = 0
    conS2 = 0
    labS2 = 0
    snpS2 = 1
    #S 3
    libS3 = 1
    conS3 = 0
    labS3 = 0
    snpS3 = 0
    #S 4
    libS4 = 1
    conS4 = 0
    labS4 = 0
    snpS4 = 0
    #S 5
    libS5 = 0
    conS5 = 1
    labS5 = 0
    snpS5 = 0
    #S 6
    libS6 = 0
    conS6 = 1
    labS6 = 0
    snpS6 = 0

    #Wales 7
    #W 1
    libW1 = 0
    conW1 = 0
    labW1 = 0
    plaW1 = 1
    #W 2
    libW2 = 0
    conW2 = 0
    labW2 = 1
    plaW2 = 0
    #W 3
    libW3 = 0
    conW3 = 0
    labW3 = 0
    plaW3 = 1
    #W 4
    libW4 = 0
    conW4 = 1
    labW4 = 0
    plaW4 = 0
    #W 5
    libW5 = 0
    conW5 = 0
    labW5 = 1
    snpW5 = 0
    #W 6
    libW6 = 0
    conW6 = 0
    labW6 = 1
    plaW6 = 0
    #W 7
    libW7 = 0
    conW7 = 1
    labW7 = 0
    plaW7 = 0

    #N.Ireland 3
    #I 1
    libI1 = 0
    conI1 = 1
    labI1 = 0
    #I 2
    libI2 = 0
    conI2 = 1
    labI2 = 0
    #I 3
    libI3 = 1
    conI3 = 0
    labI3 = 0

def TOON_SCORE(fouteLetters):
    Galgje = ('''
                       |---|
                           |
                           |            #0 fouten
                           |
                           |
                        ___|''','''

                       |---|
                       o   |
                           |            #1 fout
                           |
                           |
                    _______|''','''

                       |---|
                       o   |
                       |   |            #2 fouten
                           |
                           |
                    _______|''','''


                       |---|
                       o   |
                      /|   |            #3 fouten
                           |
                           |
                    _______|''','''


                       |---|
                       o   |
                      /|/  |            #4 fouten
                           |
                           |
                    _______|''','''

                       |---|
                       o   |
                      /|/  |            #5 fouten
                       I   |
                           |
                    _______|''','''

                       |---|
                       o   |
                      /|/  |            #6 fouten
                       II  |
                           |
                    _______|''')

    print (Galgje[len(fouteLetters)])

def TOON_DEELOPLOSSING(goedeLetters, woord):
    global WordNotFound
    partieel = len(woord)*'_'
    for i in range (0,len(woord)):
        if woord[i] in goedeLetters:
            partieel = str(partieel[0:i])+str(woord[i])+str(partieel[i+1:])
    print (partieel)
    if partieel == woord:
        print('woord gevonden, proficiat')
        WordNotFound = False
 
def GET_INPUT(prompt):
    while True:
        letter = input(prompt).lower()
        if len(letter) > 1:
            print('kies 1 enkele letter! ')
        elif letter not in list('abcdefghijklmnopqrstuvwxyz'):
            print('enkel letters uit het alfabet graag')
        elif letter in goedeLetters+fouteLetters:
            print('je hebt deze letter al eerder gekozen, kies een nieuwe letter')
        else:
            break
    return letter.lower()

def PLAY_AGAIN():
    global keeplooping
    print ('nog een partijtje Galgje? Y/N')
    antwoord= input()
    if antwoord.lower().startswith('y'):
        keeplooping = True
    else:
        print('het was leuk met jou te spelen!')


if __name__ =="__main__":
    
    keeplooping = True
    while keeplooping:
        woord ='pinguin'                                # maak hier een functie van
        WordNotFound = True
        fouteLetters = []
        TOON_SCORE(fouteLetters)
        goedeLetters = []
        TOON_DEELOPLOSSING(goedeLetters, woord)

        while keeplooping:
            gokletter =GET_INPUT('kies een letter: \n')
            if gokletter not in woord:
                fouteLetters.append(gokletter)
            else:
                goedeLetters.append(gokletter)
            TOON_SCORE(fouteLetters)
            TOON_DEELOPLOSSING(goedeLetters, woord)

            if WordNotFound == False:
                keeplooping = False
                PLAY_AGAIN()
                break
            elif len(fouteLetters) > 5:       
                print('aantal gokbeuten opgebruikt, je hangt')
                keeplooping = False
                PLAY_AGAIN()
                break
            else:
                continue








import random

def tekenBord(bord):
    print('   |   |   ')
    print(' '+bord[7]+' | '+bord[8]+' | '+bord[9]+'  ')
    print('   |   |   ')
    print('- - - - - - ')
    print('   |   |   ')
    print(' '+bord[4]+' | '+bord[5]+' | '+bord[6]+'  ')    
    print('   |   |   ')
    print('- - - - - - ')    
    print('   |   |   ')
    print(' '+bord[1]+' | '+bord[2]+' | '+bord[3]+'  ')
    print('   |   |   ')

def vraagCijfer(XofO,bord):
    print('speler, kies een cijfer (1-9):')
    keuze = int(input())
    #valideer input 1-9, bordpositie op cijfer nog niet gevuld
    return keuze

def wieBegint():
    kandidaten=['computer','speler']
    return kandidaten[random.randint(1,2)-1]

def XofO():
    print('Kies X of 0')
    XofO=str(input())
    #valideer input X of O
    return XofO.lower()

def computerZet(XofO,bord):
    print('computer, kies een cijfer (1-9):')
    keuze = int(input())
    #valideer input 1-9, bordpositie op cijfer nog niet gevuld
    return keuze

def switch(aanzet):
    if aanzet == 'speler':
        aanzet = 'computer'
    else:
        aanzet = 'speler'
    return aanzet

def spelGedaan(XofO,bord):
    print('moet dit nog verder uitwerken')
    if bord[7]==XofO and bord[8]==XofO and bord[9]==XofO:
        return 'y'

    
if __name__ == "__main__":
    bord=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    tekenBord(bord)

    spelerXofO = str(XofO())
    complement =['x','o']
    complement =[x for x in complement if x != spelerXofO]
    computerXofO = complement[0]      
    print('speler is '+spelerXofO,)
    print('computer is '+computerXofO)

    aanzet = wieBegint()
    print('aanzet is '+aanzet)

    while 1 == 1 :       
        if aanzet == 'computer':
            czet = computerZet(computerXofO, bord)
            bord[czet]=computerXofO
            tekenBord(bord)
            aanzet = switch(aanzet)
            if spelGedaan(computerXofO, bord) =='y':
                print('computer heeft gewonnen!')
                break
            
        else:
            szet = vraagCijfer(spelerXofO, bord)
            bord[szet]=spelerXofO
            tekenBord(bord)
            aanzet = switch(aanzet)
            if spelGedaan(spelerXofO, bord) =='y':
                print('speler heeft gewonnen!')
                break
    print('dit is het einde!')

    














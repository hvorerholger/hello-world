#-*- coding: utf8 -*-

def som(a,b):
    x = a + b
    return x

def gemiddelde(*getallen):
    aantal = len(getallen)
    lengte = len(getallen)
    if lengte == 0:
        return None
    som = 0
    for getal in getallen:
        if not isinstance (getal, int):
            raise TypeError("'%s' is geen geheel getal" % str(getal))
        som += getal
    return som/ aantal

#basistests
assert gemiddelde(5) == 5
assert gemiddelde(6,8) == 7
assert gemiddelde (6,7,14) == 9

#zonder invoerparameter
assert gemiddelde() == None

#meer expliciete foutboodschap
try:
    gemiddelde(6,'a',14)
except TypeError as e:
    assert str(e) == "'a' is geen geheel getal"


if __name__ == '__main__':
    #som = som (5,3)
    #print (som)

    gemiddelde(5,52,28,'p',25)
    pass

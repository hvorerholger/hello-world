#-*- coding: utf8 -*-

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

#deze in-line assert testen hergroeperen in test_gemiddeldeAssOef.py ----------------
#basistests
assert gemiddelde(5) == 5
assert gemiddelde(6,8) == 7
assert gemiddelde (6,7,14) == 9

#zonder invoerparameter
assert gemiddelde() == None

#meer expliciete foutboodschap bij fout getypeerde elementen
try:
    gemiddelde(6,'z',14)
except TypeError as e:
    assert str(e) == "'z' is geen geheel getal"
#------------------------------------------------------------------------------------

if __name__ == '__main__':
    getallen = [5,10,20,50]
    print (gemiddelde(*getallen))

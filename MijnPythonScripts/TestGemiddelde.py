def gemiddelde(*getallen):
    for getal in getallen:
        som =+ getal
    gemiddelde = som/ len(getallen)
    return gemiddelde

if __name__ == "__main__":
    x = gemiddelde(6,8)
    print(int(x))

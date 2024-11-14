def elso_karakter(string):
    """ Visszatér a string első karakterével.
    """
    return string[0]

assert elso_karakter("Hello") == "H"

def utolso_karakter(string):
    """ Visszatér az adott string utolso karakterével.
    """
    return string[-1]

assert utolso_karakter("Hello") == "o"

def legkisebb(lista):
    """ Visszatér egy számokat tartalmazó lista legkisebb számával.
    """
    legkisebbszam = 0#Elmentjuk a legkisebb számot
    for x in lista:#Végigmegyünk a listán
        if(x < legkisebbszam):#A jelenleg vizsgált szám kisebb-e mint ami el van tárolva
            legkisebbszam = x#Ha igen, akkor legyen az a szám
            #(Ha nem akkor jön a következő szám.)
    return legkisebbszam#Válasz visszatérítése

assert legkisebb( [7, 4, 9, -4, -8, 3]) == -8

def osszeg(lista):
    """ Visszatér egy számokat tartalmazó lista számainak összegével.
    """
    osszeg = 0#Osszeg elmentése
    for x in lista:#Végiglépkedés a kapott listán
        osszeg = osszeg + x#Hozzáadjuk az összeghez a jelenlegi számot.
        
    return osszeg#Válasz visszatérítése

assert osszeg( [1, 2, 3, 4, 5, 6] ) == 21

    
def halmazok_metszete(halmaz1, halmaz2):
    valasz = set()
    for i in halmaz1:
        for j in halmaz2:
            if (i == j):
                valasz.add(i)
                
    return valasz
# Az assert csak hiba esetén ad visszajelzést.

assert halmazok_metszete({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {4, 5, 6, 7}

def halmazok_unioja(halmaz1, halmaz2):
    valasz = set()
    for x in halmaz1:#Végiglépkedés a halmaz1-en
        valasz.add(x)#Hozzáadás a halmazhoz (az összes elemet)
        
    for x in halmaz2:#Végigmegyek a másik halmazon
        if(x not in halmaz1):
            valasz.add(x)
    return valasz
# Az assert csak hiba esetén ad visszajelzést.

assert halmazok_unioja({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

def faktorialis(n):
    valasz = 1
    for i in range(1, n+1):
        valasz *= i
        
    return valasz    
        

# Az assert csak hiba esetén ad visszajelzést.

assert  faktorialis(0) == 1
assert  faktorialis(1) == 1
assert  faktorialis(2) == 1 * 2
assert  faktorialis(5) == 1 * 2 * 3 * 4 * 5

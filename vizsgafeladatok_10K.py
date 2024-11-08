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


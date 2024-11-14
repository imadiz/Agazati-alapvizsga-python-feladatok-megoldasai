#Első feladat
def faktorialis(n):
    """ visszatér a paraméterként megkapott szám faktoriálisával.
    """
    # YOUR CODE HERE
    raise NotImplementedError()

assert faktorialis(0) == 1
assert faktorialis(1) == 1
assert faktorialis(2) == 1 * 2
assert faktorialis(5) == 1 * 2 * 3 * 4 * 5

#Második feladat
def lista_atlag(lista):
    """ Visszatér egy számokat tartalmazó lista számainak átlagával.
    """
    # YOUR CODE HERE
    raise NotImplementedError()

# Az assert csak hiba esetén ad visszajelzést.

assert lista_atlag([1, 2, 3, 4, 5, 6]) == 21/6

#Harmadik feladat
def halmazok_unioja(halmaz1, halmaz2):
    # YOUR CODE HERE
    raise NotImplementedError()

# Az assert csak hiba esetén ad visszajelzést.

assert halmazok_unioja({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

#Negyedik feladat
def hanyadik_a_stringben(string, betu):
    # YOUR CODE HERE
    raise NotImplementedError()

# Az assert csak hiba esetén ad visszajelzést.

assert hanyadik_a_stringben("abrakadabra", "a") == 0
assert hanyadik_a_stringben("abrakadabra", "k") == 4

#Ötödik feladat
def negativok_kivalogatasa(lista):
    # YOUR CODE HERE
    raise NotImplementedError()

# Az assert csak hiba esetén ad visszajelzést.

assert negativok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [-4, -8]
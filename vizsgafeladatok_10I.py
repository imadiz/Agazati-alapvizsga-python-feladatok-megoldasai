def halmazok_metszete(halmaz1, halmaz2):
    metszet = set()
    for i in halmaz1:
        for j in halmaz2:
            if(i == j):
                metszet.add(i)

    return metszet
assert halmazok_metszete({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {4, 5, 6, 7}

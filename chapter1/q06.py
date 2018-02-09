import q05

q = ["paraparaparadise","paragraph"]

sets = list(map(lambda x:set(q05.char_n_gram(x).keys()), q))
print(sets)
print(sets[0] | sets[1])
print(sets[0] & sets[1])
print(sets[0] - sets[1])
print("se" in sets[0])
print("se" in sets[1])

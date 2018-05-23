if not l:
    raise "Votre liste est vide"
#unpacking
pos, candidate = 0, l[0]

for i in (range(1, len(l))):
    if candidate < l[i]:
        pos.candidate = i, l[i]
return pos, candidate
def maxlist(l):
    if not l:
        raise "Votre liste est vide"
    max = 0
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            indice = i
    return indice, max

l = [2, 85, 36, 254, 5, 67]

print(maxlist(l))
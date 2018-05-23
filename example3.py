def h(a,b,c):

    return {'a' : a, 'b' : b, 'c' : c}

print(h(a = 10, c = 20, b = 30))

def position(*coord):

    try:
        x, y, z = coord

        print(x)
        print(y)
        print(z)

    except ValueError:
        print("nombre d'argument invalide")


position(1,2,3,4)
position(1,2,3)
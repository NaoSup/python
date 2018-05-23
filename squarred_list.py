[x**2 for x in range(10)]
[x**2 for x in range(10) if x%2 == 0]

def verify(x):
    if x % 2 == 0:
        return True
    else:
        return False

[x**2 for x in range(10) if verify(x)]

[(x,y) for x in range(10) for y in range(5)]

sum(x**2 for x in range(11))
sum(x for x in range(11))


m1 = (1, 2, 3)
m2 = (2, 3, 4)

def multi_tuples(m1, m2):

    if len(m1) == len(m2):

        return sum(m1[x]*m2[x] for x in range(len(m1)))

print(multi_tuples(m1,m2))

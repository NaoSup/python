#github prof : antoine07

#variables globales
a = 11
b = 22

#def est le mot clé pour définir une fonction
def f():
    #variable englobante
    b = 1
    #variable locale
    c = 33
    def g():
        print(a) #affiche 11
        print(b) #affiche 1
    g()
f()

try:
    print(c) #n'est pas défini
except NameError:
    print("c n'est pas définie")

import builtins

print = 1 #ne pas faire même si c'est possible

print("Hello ne marche plus")
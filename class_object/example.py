class Model:
    a = 1
    def __init__(self, info):
        self.info = "coucou toi"

    def __len__(self):
        return len(self.info)

    def __contains__(self, str):
        return str in self.info

    def __str__(self):
        return "Wow ! J'ai fait un print sur l'objet"

    #self = référence à l'instance -> définir méthode appelée à partir de l'objet
    def hello(self, message):
        print(f'Hey {message} !')

#initialisation de la classe
m = Model("dadidadida")
m.hello("You")

#accès à la valeur de l'attribut
print(m.info)

print(m.a)
print(Model.a)

print(len(m))

print(m)

print("toi" in m)
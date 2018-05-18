def comptStr(string):
    dict = {}
    list = string.split(' ')
    for i in range(len(list)):
        key = list[i]
        value = 0
        for letters in key:
            value += 1
        dict[key] = value
    return dict

string = "Hello tout le monde" 
print(comptStr(string))

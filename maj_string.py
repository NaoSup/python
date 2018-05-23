def upper_word(word):
    if word.isupper():
        result = 'true'
    else:
        result = 'false'
    return result

true = 'CECI EST UN TEST TRUE'
false = 'CECI est un test false'

print(upper_word(true))
print(upper_word(false))
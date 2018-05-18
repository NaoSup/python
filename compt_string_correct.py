phrase = "Hello tout le monde".split(' ')

def comptWordsPhrase(phrase):
    d = {}
    for word in phrase:
        d[word]=len(word)
    return d

print(comptWordsPhrase(phrase))
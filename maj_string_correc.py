def is_upper(l):
    if not l:
        raise "Liste vide attention..."
    
    return all(ord(ch) in range(65,91) for ch in l)
word = "TEsT"
print(is_upper(word))

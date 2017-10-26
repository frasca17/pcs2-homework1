def capitalize(string):
    l= []
    letter = string.split(' ')
    for c in letter:
        l.append(c.capitalize())
    return ' '.join(l)
def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score= 0
    for c in range(len(string)):
        if string[c] in vowels:
            kevin_score += (len(string) - c)
        elif string[c] not in vowels:
            stuart_score += (len(string) - c)
            
    if kevin_score > stuart_score:
        print 'Kevin', kevin_score
    elif kevin_score < stuart_score:
        print 'Stuart', stuart_score
    else:
        print 'Draw'
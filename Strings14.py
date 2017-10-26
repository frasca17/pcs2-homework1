def merge_the_tools(string, k):
    for c in range(len(string)/k):
        u = ''
        for c in string[c * k : (c+1) * k]:
            if c in u:
                continue
            u = u + c
        print u
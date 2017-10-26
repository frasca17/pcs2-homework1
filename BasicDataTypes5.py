scores= list()
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    scores.append([name, score])

seclow= sorted(list(set([score for name, score in scores])))[1]
result= sorted([name for name, score in scores if score == seclow])
print '\n'.join(result)
result = input()
score=0
tmp_score=0
for x in result:
    if x =='O':
        tmp_score += 1
        if tmp_score > score:
            score = tmp_score
    else:
        tmp_score = 0
print(score)
# 2차원배열 인접한 원소 비교 - 좌우, 가장자리도 비교
n = int(input())
m = int(input())
li = []
result = 0
for _ in range(n):
    in_li = list(map(int,input().split()))
    li.append(in_li)

for i, row in enumerate(li):
    for j, val in enumerate(row):
        if j>0:
            left = row[j-1]
        else:
            left = -1
        # 만약 3항으로 한다면, left = row[j-1] if j > 0 else -1
        if j < m - 1:
            right = row[j+1]
        else:
            right = -1
        
        if val > left and val > right:
            result += 1

print(result)

## 상하 추가 한다면,                                                                                                        
#          if i > 0:
#              up = li[i-1][j]                                                                                                    
#          else:                                                                
#              up = -1
#          if i < n - 1:
#              down = li[i+1][j]
#          else:
#              down = -1
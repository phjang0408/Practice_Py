diff = [10,15] #날씨 1,2 초기
c_for_m = [[0,2],[1,2],[0,1]]# 산 1,2,3 / 코스 1,2
total_d = 0
total = 0

n = int(input())
for _ in range(n):
    m = int(input())
    c = int(input())
    w = int(input())
    d = int(input())
    
    x = c_for_m[m-1][c-1]
    y = (diff[w-1] + x*5)
    
    if total_d >= 20:
        y -= 2
    total_d+=d
    y *= d
    total += y
    
print(total)
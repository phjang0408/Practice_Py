# 문자열 뒤집기, 비교
n = int(input())
cnt = 0
for _ in range(n):
    st = input()
    r_st = st[::-1]
    if r_st == st:
        cnt+=1
print(cnt)
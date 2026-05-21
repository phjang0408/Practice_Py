# 딕셔너리 구성 [문자열-정수], 같은 키면 value 누적, 이후 특정 키 조회
history = {}
n = int(input())
for _ in range(n):
    k,v = input().split()
    v = int(v)
    if k in history:
        history[k] += v
    else:
        history[k] = v
        
name = input()
print(history.get(name,0))
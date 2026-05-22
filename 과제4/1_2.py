n = int(input())
over_time = 0
total_cal = 0
for _ in range(n):
    l = int(input())
    m = int(input())
    h = int(input())
    cal = l*2+m*6+h*10

    # 순서대로 처리 → 누적 상태 유지 → 임계값 초과 시 동작 변경 
    if over_time > 30:
        cal //= 2
    total_cal += cal
    over_time += (l+m+h)
print(total_cal)
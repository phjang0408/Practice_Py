n = int(input())
over_time = 0
total_cal = 0
set_time = [0,0]
plus_cal = 0
for _ in range(n):
    l = int(input())
    m = int(input())
    set_time[0] += m
    h = int(input())
    set_time[1] += h

    cal = l*2+m*6+h*10

    if over_time > 30:
        cal //= 2
    total_cal += cal
    over_time += (l+m+h)

if over_time > 30:
    plus_cal += set_time[0]*3+set_time[1]*5
total_cal += plus_cal
print(total_cal)
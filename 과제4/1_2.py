def check_time(time_value, Over):
    if (Over + time_value) >= 30:
        time_value = time_value - (30 - Over)
        Over = 30
    else:
        Over += time_value
    return time_value, Over

def calculate_cal(l, m, h, Over):
    if Over >= 30:
        return l * 1 + m * 3 + h * 5
    else:
        return l * 2 + m * 6 + h * 10

n = int(input())
Over = 0
cal = 0

for _ in range(n):
    l, Over = check_time(int(input()), Over)
    m, Over = check_time(int(input()), Over)
    h, Over = check_time(int(input()), Over)
    cal += calculate_cal(l, m, h, Over)

print(cal)
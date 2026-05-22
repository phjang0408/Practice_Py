d = [31,28,31,30,31,30,31,31,30,31,30,31]

b_y = int(input())
b_m = int(input())
b_d = int(input())

n = int(input())
for _ in range(n):
    c_y = int(input())
    if c_y // 10000 == 0:
        c_m = int(input())
        c_d = int(input())
    else:
        c_m = c_y % 10000 // 100
        c_d = c_y % 100
        c_y //= 10000
    
    if (b_y,b_m,b_d) > (c_y,c_m,c_d) :
        print("Error")
    else:
        b_total = 365*b_y + sum(d[:b_m-1]) + b_d
        c_total = 365*c_y + sum(d[:c_m-1]) + c_d
        result = c_total - b_total
        print(result)
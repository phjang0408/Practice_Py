m = [5000,5500,6500,7000,6800]
d = [300,300,250,500,400,500,0]
t = [1000,1200,800,1100,1050,1150,900,600,750]
b = [2000,1800,500]
total = 0
n = int(input())
for _ in range(n):
    o_m = int(input())
    o_t = int(input())
    o_d = int(input())
    o_b = int(input())
    total += m[o_m-1] + d[o_d-1] + t[o_t-1] + b[o_b-1]
print(total)
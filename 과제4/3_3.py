m = [5000,5500,6500,7000,6800]
d = [300,300,250,500,400,500,0]
t = [1000,1200,800,1100,1050,1150,900,600,750]
b = [2000,1800,500]
total = 0
n = int(input())
for _ in range(n):
    o_m = int(input())
    o_t1 = int(input())
    o_t2 = int(input())
    o_d = int(input())
    o_b = int(input())
    total += m[o_m-1] + d[o_d-1] + t[o_t1-1] + t[o_t2-1] + b[o_b-1]

tax = (total + 0.5) // 11
total_notax = (total+0.5) * 10 // 11
print("-----HongSalad-----")
print("Salad Qty: %d"%n)
print("-------------------")
print("Total Price: %d" % total_notax)
print("Tax(10%%): %d"% tax)
print("-------------------")
print("Total: %d" % (total_notax + tax))
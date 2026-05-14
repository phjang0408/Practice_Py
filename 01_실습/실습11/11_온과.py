A = []
NUM_JEWEL = 3
Name = ['diamond', 'ruby', 'emerald']
Cost = [100, 60, 30]
Cost_Mag = 2
Total_sales = 0
Total_costs = 0
for i in range(NUM_JEWEL):
    x = int(input())
    A.append(x)
    Total_costs += Cost[i]*x
    
for Jewel_Name in range(NUM_JEWEL):
    Selling = input()
    Total_sales += A[Name.index(Selling)]*Cost[Name.index(Selling)]*Cost_Mag
    Cost_Mag += 1
print("Total sales = %d" % Total_sales)
print("Total costs = %d" % Total_costs)

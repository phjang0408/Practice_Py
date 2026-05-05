cost = [[5000,8000],[15000,20000],[30000,45000]]
milage = [500,2000,5000]
Total_Cost = 0
Total_Milage = 0
n = int(input())
for i in range(n):
    act_Num = int(input()) - 1
    act_Month = int(input())
    if act_Month in [1,2,8,9]:
        Total_Cost += cost[act_Num][1]
    else:
        Total_Cost += cost[act_Num][0]
    Total_Milage += milage[act_Num]
print(Total_Cost)
print(Total_Milage)
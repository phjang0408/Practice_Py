#정수 N을 입력받은 후, N개의 정수를 입력받아 빈 리스트에 차례로 추가하라.
#이후 해당 리스트에서 가장 큰 수와, 그 수가 처음 등장하는 원소 번호를 출력하라.
#(단, 리스트 안의 모든 수는 1 이상의 정수이다.)
n = int(input())
li = []
max_num = 0
pos = 0
for i in range(n):
    li.append(int(input()))
    if max_num < li[i]:
        max_num=li[i]
        pos = i
print(f"Max = {max_num}")
print(f"Pos = {pos}")
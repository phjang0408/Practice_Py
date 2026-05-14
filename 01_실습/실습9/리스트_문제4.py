#정수 N을 입력받고, N개의 정수를 입력받아 빈 리스트에 차례로 추가한다.
#리스트에서 최솟값과 최댓값을 삭제하고, 삭제가 완료된 리스트를 출력한다.
#(단, N은 2 이상의 정수이다. 리스트의 원소에 중복되는 수는 주어지지 않는다.)
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.remove(max(li))
li.remove(min(li))

print(li)
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
print(li)
r_li = []
for i in range(n):
    r_li.append(li.pop())
print(r_li)
#정수 N을 입력받고, N개의 정수를 입력받아 빈 리스트에 차례로 추가한다.
#추가가 완료된 리스트를 출력하고, 리스트 안의 수들을 역순으로 다른 리스트에 저장한다.
#그 후에는 원소들을 역순으로 저장한 리스트를 출력하여라.
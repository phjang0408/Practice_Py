#정수 N을 입력받고, 1부터 N까지의 정수를 빈 리스트에 차례로 추가한다.
#이후 N-1개의 정수를 입력받아 리스트에서 삭제한 후, 원소가 하나만 남은 리스트를 출력한다.
#(단, N-1개의 정수는 1부터 N까지의 범위 안에 반드시 속하며, 중복된 값은 주어지지 않는다.)

n = int(input())
li = []
for i in range(1,n+1):
    li.append(i)
for i in range(n-1):
    li.remove(int(input()))
    
print(li)
# A번 원소부터 B번 원소까지를 담은 부분 리스트
N = int(input())
li = []
for i in range(1,N+1):
    li.append(i)
print(li)
a = int(input())
b = int(input())

print(li[a:b+1])
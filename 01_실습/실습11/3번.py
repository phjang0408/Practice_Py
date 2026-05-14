# 리스트에서 최대, 최소 모두 제거하기
# 최대, 최소는 여러개 있음
li=[]
while True:
    x = int(input())
    if x == 0:
        break
    li.append(x)
print(li)

t_max = max(li)
t_min = min(li)
new_li = []
for x in li:
    if x == t_max or x == t_min:
        continue
    new_li.append(x)
print(new_li)

# 리스트를 순환중에 삭제하면 안 된다! -> 인덱스 오류남
# t_max = max(li)
# t_min = min(li)
# for x in li:
#     if x == t_max or x == t_min:
#         li.remove(x)
# print(li)
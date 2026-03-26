# 리스트 관련 함수
a = [3,1,2,5,4]

# 1. 추가 - append, insert, extend
a.append(6)         # append : 뒤에 추가
print(a)
a.insert(6,7)       # insert : 추가할 위치, 추가할 값
print(a)
a.extend([8,9])     # extend : 배열을 뒤에 붙임

# 2. 정렬 - sort
a.sort()            #
print(a)

# 3. 뒤집기 - reverse
a.reverse()         #
print(a)

# 4. index구하기 - index
print(a.index(4))   #

# 5. 제거 - remove
a.remove(1)         #
print(a) 
a.pop()             #
print(a) 

# 6. 원소 세기 - count
print(a.count(3))   #
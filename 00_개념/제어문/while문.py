# 1. 기본 형태
a = 3
while a > 0:
    print(a)
    a -= 1   # python은 증감 연산자가 없음

# 2. [while-else 형태] - while이 정상적으로 끝나면(break없이), else 문 실행
count = 0
while count < 3:
    print(f"카운트 : {count}")
    count +=1
else:
    print("While문이, break 없이, 정상 종료되었습니다.")
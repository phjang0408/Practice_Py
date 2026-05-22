d = [31,28,31,30,31,30,31,31,30,31,30,31]

b_y = int(input())
b_m = int(input())
b_d = int(input())

c_y = int(input())
c_m = int(input())
c_d = int(input())

# 튜플은 왼쪽 값부터 계산
if (b_y,b_m,b_d) > (c_y,c_m,c_d) :
    print("Error")
else:
    # 차이, 간격을 1차원으로 풀어서 계산
    # 복잡한 구조(연/월/일) → 단일 숫자(총 일수) → 단순 빼기
    b_total = 365*b_y + sum(d[:b_m-1]) + b_d
    c_total = 365*c_y + sum(d[:c_m-1]) + c_d
    result = c_total - b_total
    print(result)

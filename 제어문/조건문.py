# 1. python의 조건연산자 : [and, or, not] 리터럴임, &&, ||, ! 아님
money = 2000
card = True
if money >1000 and card:
    print("I can go!")

# 2. in, not in => x in (리스트, 튜플 문자열)이면, 포함 여부를 확인하고, bool 반환
if 2 in [1,2,3]:
    print("2 in li")
    
tu = ('a','b','c')
if 'c'in tu:
    print("c is tuple")

if 'k' not in 'python':
    print("문자열과 not in")
    
# 3. pass - 아무것도 안 할 때
pocket = ['paper','money','card']
if 'card' in pocket:
    pass    # 참이면 건너뛰어라
else:
    print("카드를 꺼내라")
    
# 4. if - elif - else로 씀

# 5. 조건표현식 : [순서 다름!] => 참일때 실행할 식 (if) 조건식 (else) 거짓일 때 실행할 식
power = 100
print("POWER!!!") if power > 50 else print("Not enough...")
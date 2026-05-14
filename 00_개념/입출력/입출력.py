# input()은 [문자열]로 기본 저장
a = input("input안의 문자열입니다. 입력하세요 : ")
print(a)

# 형 변환
age = input("나이를 입력하세요 : ")
age = int(age)
print(age+1)

height = float(input())
print("height : ", height / 100)

print(f"{age}")
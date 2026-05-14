# 기본
a = 1
print(a)
a = "hello"
print(a)
a=[1,2,3]
print(a)

# 큰 따옴표 열거형은 +와 동일
print("Life""is""short")
print("Life"+"is"+"short")  ## 위와 동일한 결과

# 쉼표로 띄어쓰기 가능
print("Life","is","short")

# sep으로 구분자(쉼표에 들어갈 문자) 설정
print("2026","03","12", sep = '-')
print("Jump","python", sep = " TO ")

# Print를, 한 줄에 출력 : end 사용
for i in range(10):
    print(i, end = ' ')
# 파일에서 n개의 문자만 읽기
file = open('test.txt', 'w')
file.write("Hello, This is Python Programming.")
file.close()

n = int(input())
f_r = open('test.txt','r')
result = f_r.read(n)
print(result)
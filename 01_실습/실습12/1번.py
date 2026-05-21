# [시작] 파일_객체_이름 = open(파일_이름, 파일_열기_모드)
# 파일 이름과 같은 파일이 없으면, 새로 만듬
# [종료] = 파일_객체_이름.close()
# 모드 -> r : read, w : write, a : add
file_name = input()
n = int(input())
m = int(input())

f = open(file_name,'w')
numbers = " ".join(str(i) for i in range(n,m+1)) #구분자.join : 구분자 문자열로 이어붙히기

f.write(numbers)
f.close()

f_r = open(file_name, 'r')
line = f_r.read()
print(line)
f_r.close()
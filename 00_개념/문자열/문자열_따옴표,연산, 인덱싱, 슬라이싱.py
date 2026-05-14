# [따옴표]
ood = "it's favorite food" # 큰따옴표 안 작은따옴표
say = '"Easy!" he says'     # 작은따옴표 안 큰 따옴표
food = 'it\'s favorite food'        # 역슬래시

multiline = '''
he says
Easy!
'''     # 큰 따옴표도 가능
# 역슬래시 -> \n, \t, \\, \', \" 등
# [%는 %%로 보간!]

tmp_string = "abcdefghijklmn"

# [문자열 더하기]
print(tmp_string + say)   # 더하기
print(tmp_string * 2)     # 곱하기
print(len(tmp_string))    # 길이 구하기

# [인덱싱, 슬라이싱]
print(tmp_string[0])      # 인덱싱 (배열처럼 생각)
print(tmp_string[-1])     # 인덱싱 (음수는 뒤부터, -1로 시작)
slic = tmp_string[0:4]    # 슬라이싱 [마지막 인덱스는 포함 X!!]
print(slic)    
slic = tmp_string[4:]     # 시작이나 끝 생략
print(slic)  
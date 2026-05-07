# 자리수 합
def get_digit_sum(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result
Se = int(input())
Da = int(input())
score_s = get_digit_sum(Se)
score_d = get_digit_sum(Da)
if score_s == score_d:
    print("Draw")
elif score_s > score_d:
    print("Sejong Win")
else:
    print("Daeyang Win")
    
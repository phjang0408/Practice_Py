def isPrime(x):
    if x ==1:
        return False
    if x == 2:
        return True
    for i in range(2,x):
        if i*i > x:
            break
        if x%i == 0:
            return False
    return True
num = int(input())
if isPrime(num):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
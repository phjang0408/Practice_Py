import matplotlib.pyplot as plt
n = int(input())
x = list(range(-n, n+1))
y = [i**2 for i in x]

plt.plot(x,y,color = 'red')
plt.title('y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
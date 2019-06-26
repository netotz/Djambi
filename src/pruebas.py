from math import sqrt, pi

suma = 0.0
for i in range(1,10000000):
	suma += 1/(i**2)
num = sqrt(6*suma)

print(num)
print(pi)
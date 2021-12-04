import math

print('Task 1\n')

x = int(input('Введите x: '))
n = int(input('Введите n: '))

y = 0

for i in range (1, n+1, 2):
  y += x/i

print('\nY = ', y)

print('\nTask 2\n')

# Исходные данные:
a = -2
b = 5
n = 14

k = (b - a)/n
x = a

for i in range (n+1):
  f_1 = abs((x+10)**5)
  f_2 = math.exp(-(x+5))
  print('x = ', x)
  print('F1 = ', f_1)
  print('F2 = ', f_2, '\n')
  x += k

# Sorting three 🌶️
# Write a program that orders three numbers from largest to smallest.

# Сортировка трёх 🌶️
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())
x = max(a, b, c)
n = min(a, b, c)
s = (a+b+c)-x-n
print(x)
print(s)
print(n)


Sample Input 1:
132
129
135
Sample Output 1:
135
132
129
Sample Input 2:
150
160
156
Sample Output 2:
160
156
150
Sample Input 3:
161
139
148
Sample Output 3:
161
148
139

Суммы двух
На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел. Напишите программу, 
которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
# Sum of two
# The program input is a natural number n, where n≥2. Then n integers arrive. Write a program
# which creates a list from the specified numbers, consisting of the sums of neighboring numbers (0 and 1, 1 and 2, 2 and 3, etc.).

a = []  
n = int(input())
s = 0
for i in range(n):
    v = int(input())
    d = s + v
    s = v
    a.append(d)
print(a[1:])


Sample Input 1:
5
1
2
3
4
5
Sample Output 1:
[3, 5, 7, 9]
Sample Input 2:
2
10
9
Sample Output 2:
[19]

# No zeros
Без нулей
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
Примечание 1. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
Примечание 2. Отличные от нуля числа – те числа, которые не равны нулю.
# Write a program that reads 10 numbers and prints the product of non-zero numbers.
# Note 1. It is guaranteed that at least one of the 10 numbers is non-zero.
# Note 2: Non-zero numbers are those numbers that are not equal to zero.

  
total = 1  
for i in range(1, 11):
    n = int(input())
    if n != 0:
        total *= n
print(total)

  
Sample Input 1:
8
0
1
2
1
0
0
5
4
12
Sample Output 1:
3840
Sample Input 2:
1
43
2
234
78
0
1
1
23
4
Sample Output 2:
144409824
Sample Input 3:
3
8
66
1110
4
2
2
1
0
0
Sample Output 3:
28131840

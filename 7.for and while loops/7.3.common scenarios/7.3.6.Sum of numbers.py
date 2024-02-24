# Sum of numbers
# Сумма чисел
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. 
Напишите программу, которая подсчитывает сумму введенных чисел (не включая само число n). 
# The input to the program is a natural number n, and then n integers, each on a separate line. 
# Write a program that calculates the sum of the numbers entered (not including the number n itself).


total = 0 
n = int(input())
for i in range(n):
    n = int(input())
    total += n
print(total)


Sample Input:
5
3
2
1
0
-1
Sample Output:
5

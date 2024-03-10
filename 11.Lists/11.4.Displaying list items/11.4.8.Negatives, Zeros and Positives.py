Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, 
а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
# The input to the program is a natural number n, and then n integers. Write a program that prints all negative numbers first, then zeros,
# and then all the positive numbers, each on a separate line. The numbers must be output in the same order in which they were entered.

n = int(input()) 
a = []
b = []
c = []
for i in range(n):
    s = int(input())
    if s == 0:
        b.append(s)
    elif s > 0:
        c.append(s)
    elif s < 0:
        a.append(s)
print(*a, sep='\n')
print(*b, sep='\n')
print(*c, sep='\n')

  
Sample Input 1:
7
3
-4
1
0
-1
0
-2
Sample Output 1:
-4
-1
-2
0
0
3
1
Sample Input 2:
5
4
3
-2
-10
0
Sample Output 2:
-2
-10
0
4
3

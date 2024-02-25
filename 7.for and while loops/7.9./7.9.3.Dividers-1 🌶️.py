# Dividers-1 🌶️
# The input to the program is two natural numbers a and b (a< b). Write a program that finds a natural number from the segment [a;b]
# with the maximum sum of divisors and the sum of its divisors. If there are several such numbers, print the largest of them.
Делители-1 🌶️
На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит натуральное число из отрезка [a;b] 
с максимальной суммой делителей и сумму его делителей. Если таких чисел несколько, то выведите наибольшее из них.

  

a = int(input())
b = int(input())
a<b
x=0
total=0
total1=0
x1=0

for i in range(a,b+1):
    total=0
    for j in range(1,i+1):
        if i%j == 0:
            total+=j
            x=i           
            if total>=total1:
                total1=total
                x1=x
print(x1, total1,end='')


  
Sample Input 1:
1
10
Sample Output 1:
10 18
Sample Input 2:
1
100
Sample Output 2:
96 252

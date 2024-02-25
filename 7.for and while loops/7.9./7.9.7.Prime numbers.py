# Prime numbers
# The input to the program is two natural numbers a and b (a< b). Write a program that finds all prime numbers from a to b inclusive.
# Note. The number 1 is not prime.
Простые числа
На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит все простые числа от a до b включительно.
Примечание. Число 1 простым не является.



a = int(input())
b = int(input())
a<b
for i in range(a, b+1):
    if i>1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
                print(i)
          


Sample Input 1:
2
15
Sample Output 1:
2
3
5
7
11
13
Sample Input 2:
1
5
Sample Output 2:
2
3
5

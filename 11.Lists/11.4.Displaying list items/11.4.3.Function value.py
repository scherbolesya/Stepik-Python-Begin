Значение функции
# Function value
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, 
которая для каждого введенного числа x выводит значение функции f(x)=x**2+2x+1, каждое на отдельной строке.
# The input to the program is a natural number n, and then n integers. Write a program
# which for each entered number x displays the value of the function f(x)=x**2+2x+1, each on a separate line.

n = int(input())
s1 = []
s2 = []
for i in range(n):
    s = int(input())
    s1.append(s)
    a = s*s+2*s+1
    s2.append(a)
print(*s1, sep='\n')
print()
print(*s2, sep='\n')


Sample Input 1:
5
1
2
3
4
5
Sample Output 1:
1
2
3
4
5

4
9
16
25
36
Sample Input 2:
3
10
20
30
Sample Output 2:
10
20
30

121
441
961

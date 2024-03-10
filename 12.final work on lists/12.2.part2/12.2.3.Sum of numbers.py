# Sum of numbers
Сумма чисел
На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, 
а затем вычисляет сумму полученных чисел.
Примечание. Строковый метод join() работает только со списком строк.
# The input to the program is a string of text containing natural numbers. Write a program that inserts a + sign between each number,
# and then calculates the sum of the resulting numbers.
# Note. The string join() method only works on a list of strings.

s = [int(i) for i in input().split()]
s1 = 0
for i in range(len(s)):
    s1 += s[i]
print(*s, sep='+',end='')
print('=',s1, sep='')


Sample Input 1:
2 5 11 33 55
Sample Output 1:
2+5+11+33+55=106
Sample Input 2:
1 1 1
Sample Output 2:
1+1+1=3

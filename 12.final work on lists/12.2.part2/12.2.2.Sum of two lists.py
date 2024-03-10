# Sum of two lists
Сумма двух списков
На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. 
Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. 
Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
Примечание. Количество чисел в обеих строках одинаковое.

# The program receives two lines of text containing integers as input. Lists of numbers L and M are formed from these lines.
# Write a program that creates a third list whose elements are the sums of the corresponding elements of lists L and M.
# Next, the program should display each element of the resulting list on one line, separated by 1 space.
# Note. The number of numbers in both lines is the same.

s = [int(i) for i in input().split()]
s1 = [int(i) for i in input().split()]
s2 = []
for i in range(len(s)):
    a = s[i] + s1[i]
    s2.append(a)
print(*(s2))


Sample Input 1:
3 1 4
1 5 9
Sample Output 1:
4 6 13
Sample Input 2:
1 1 1 1 1 1
9 9 9 9 9 9
Sample Output 2:
10 10 10 10 10 10

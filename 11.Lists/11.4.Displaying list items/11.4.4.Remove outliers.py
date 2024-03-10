Remove outliers
При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет наименьшее 
и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
# When analyzing data collected as part of a scientific experiment, it can be useful to remove the largest and smallest values.
# The input to the program is a natural number n, and then n different natural numbers. Write a program that removes the smallest
# and the largest value of the specified numbers, and then displays the remaining numbers each on a separate line, without changing their order.

b = int(input())
n = []
for i in range(b):
    a = int(input())
    n.append(a)
n.remove(max(n))
n.remove(min(n))
print(*n, sep='\n')


Sample Input:
10
9
17
189
3
55
78
11
7
888
160
Sample Output:
9
17
189
55
78
11
7
160

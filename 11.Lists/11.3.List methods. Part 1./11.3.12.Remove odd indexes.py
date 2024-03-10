# Remove odd indexes
# The input to the program is a natural number n, and then n integers. Write a program that creates a list from the given numbers,
# then removes all elements at odd indexes, and then prints the resulting list.
Удалите нечетные индексы
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список, 
затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

n = int(input())
a = []
for i in range(n):
    s = int(input())
    a.append(s)
del a[1::2]
print(a)

  
Sample Input 1:
10
0
1
2
3
4
5
6
7
8
9
Sample Output 1:
[0, 2, 4, 6, 8]
Sample Input 2:
1
8
Sample Output 2:
[8]
Sample Input 3:
2
9
6
Sample Output 3:
[9]

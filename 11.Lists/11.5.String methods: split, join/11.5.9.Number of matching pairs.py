# Number of matching pairs
Количество совпадающих пар
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. 
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# The input to the program is a text string containing integers. A list of numbers is formed from this string.
# Write a program that counts how many pairs of elements in the resulting list are equal to each other.
# It is believed that any two elements equal to each other form one pair that must be counted.

a = input().split()
print(sum(a.count(x)-1 for x in a)//2)


Sample Input 1:
1 7 5 7 5
Sample Output 1:
2
Sample Input 2:
3 3 3 3 3
Sample Output 2:
10
Sample Input 3:
8 7 6
Sample Output 3:
0

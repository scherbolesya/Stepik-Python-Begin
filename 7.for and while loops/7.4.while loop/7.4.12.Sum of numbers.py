# Sum of numbers
Сумма чисел
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. 
Признаком окончания последовательности является любое отрицательное число, при этом в саму последовательность оно не входит. 
Напишите программу, которая выводит сумму всех членов данной последовательности.
Примечание. Число 0 не является признаком окончания последовательности.
# The input to the program is a sequence of integers, each number on a separate line.
# A sign of the end of a sequence is any negative number, although it is not included in the sequence itself.
# Write a program that prints the sum of all terms of a given sequence.
# Note. The number 0 does not indicate the end of the sequence.

  
a = int(input())
total = 0
while a >= 0:
    total += a
    a = int(input())
print(total)

  
Sample Input 1:
1
2
3
4
5
6
7
8
9
10
-5
45
2
3
Sample Output 1:
55
Sample Input 2:
4
-5
Sample Output 2:
4
Sample Input 3:
10
10
-6
43
Sample Output 3:
20

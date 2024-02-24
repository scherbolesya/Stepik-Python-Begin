# While we're sharing
Пока делимся
На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке. 
Концом последовательности является любое число, не делящееся на 7 (само это число в последовательность не входит, лишь символизируя её конец). 
Напишите программу, которая выводит члены данной последовательности.
# The input to the program is a sequence of integers divisible by 7, each number on a separate line.
# The end of the sequence is any number that is not divisible by 7 (this number itself is not included in the sequence, only symbolizing its end).
# Write a program that prints the members of a given sequence.


a = int(input())
while a%7==0:
    print(a)
    a = int(input())
  

Sample Input 1:
49
2401
4809
0
2
10
100
Sample Output 1:
49
2401
4809
0
Sample Input 2:
7
7
14
21
13
21
12
45
56
7
7
Sample Output 2:
7
7
14
21
Sample Input 3:
7
8
9
8
Sample Output 3:
7

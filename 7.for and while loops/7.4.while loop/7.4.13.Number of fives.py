# Number of fives
Количество пятерок
На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. 
Концом последовательности является любое неположительное число либо число, большее 5. Напишите программу, которая выводит количество пятерок.
Примечание. Не забываем, что неположительными числами являются все отрицательные числа и число 0. 😉
# The input to the program is a sequence of integers from 1 to 5, characterizing the student’s grade, each number on a separate line.
# The end of the sequence is any non-positive number or a number greater than 5. Write a program that prints the number of fives.
# Note. Don't forget that non-positive numbers are all negative numbers and the number 0. 😉


a = int(input())
total = 0
while 0<a and a<6:
    if a==5:
        total += 1
    a = int(input())
print(total) 


Sample Input 1:
1
1
2
2
3
4
4
5
5
5
5
-17
1
2
5
4
Sample Output 1:
4
Sample Input 2:
5
5
-9
5
5
Sample Output 2:
2
Sample Input 3:
5
1
0
5
5
3
-2
Sample Output 3:
1

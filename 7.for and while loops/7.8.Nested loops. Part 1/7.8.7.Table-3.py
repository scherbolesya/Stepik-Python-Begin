# Table-3
# Given a natural number n (n≤ 9). Write a program that prints an addition table for all numbers from 1 to n (inclusive) as per the example.
# Note 1. We mean the addition table from 1 to 9 (inclusive).
# Note 2: There may be a space at the end of the line.
Таблица-3
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n (включительно) в соответствии с примером.
Примечание 1. Таблицу сложения подразумеваем от 1 до 9 (включительно).
Примечание 2. В конце строки может быть пробел.


n = int(input())
for i in range(1,n+1):
    for k in range(1,10):
        for j in range(n):
            print(i,'+', k, '=', i+k)
            break
    print()


Sample Input 1:
1
Sample Output 1:
1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
1 + 7 = 8
1 + 8 = 9
1 + 9 = 10
Sample Input 2:
3
Sample Output 2:
1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
1 + 7 = 8
1 + 8 = 9
1 + 9 = 10

2 + 1 = 3
2 + 2 = 4
2 + 3 = 5
2 + 4 = 6
2 + 5 = 7
2 + 6 = 8
2 + 7 = 9
2 + 8 = 10
2 + 9 = 11

3 + 1 = 4
3 + 2 = 5
3 + 3 = 6
3 + 4 = 7
3 + 5 = 8
3 + 6 = 9
3 + 7 = 10
3 + 8 = 11
3 + 9 = 12

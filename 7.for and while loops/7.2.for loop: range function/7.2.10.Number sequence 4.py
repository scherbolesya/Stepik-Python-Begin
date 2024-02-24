# Number sequence 4
# Последовательность чисел 4
Даны два натуральных числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно, удовлетворяющие хотя бы одному из условий:
число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.
Примечание. Если нет чисел, удовлетворяющих условию, выводить ничего не надо.

# Given two natural numbers m and n (m≤n). Write a program that prints all integers from m to n inclusive that satisfy at least one of the following conditions:
# the number is a multiple of 17;
# the number ends in 9;
# number is a multiple of 3 and 5 at the same time.
# Note. If there are no numbers that satisfy the condition, there is no need to output anything.

  
m, n = int(input()), int(input())  #Последовательность чисел 4
for i in range(m,n+1):
    if i%17 ==0 or i % 15 ==0 or i%10 == 9:
        print(i)

  
Sample Input 1:
1
20
Sample Output 1:
9
15
17
19
Sample Input 2:
17
17
Sample Output 2:
17
Sample Input 3:
19
19
Sample Output 3:
19

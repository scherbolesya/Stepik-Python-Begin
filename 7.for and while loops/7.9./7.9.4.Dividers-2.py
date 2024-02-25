# Dividers-2
# The program input is a natural number n. Write a program that displays a graphical representation of the divisibility of numbers from 1 to n inclusive.
# In each line you need to print the next number and as many “+” symbols as there are divisors for this number.
Делители-2
На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. 
В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.



n = int(input()) 
counter = 0
for i in range(1,n+1):
    counter=0
    for j in range(1,i+1):
        if i%j==0:
            counter+=1
    print(i,counter * '+',sep='')
  


Sample Input:
5
Sample Output:
1+
2++
3++
4+++
5++

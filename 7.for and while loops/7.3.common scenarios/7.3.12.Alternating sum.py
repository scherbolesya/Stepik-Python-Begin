# Alternating sum
Знакочередующаяся сумма
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы: 1−2+3−4+5−6+…+(−1)**(n+1)⋅n
Примечание. Рассмотрим более подробно 2-й тест. Для числа n=5 у нас будет такая сумма: 1−2+3−4+5=3.
# The program input is a natural number n. Write a program to calculate the alternating sum: 1−2+3−4+5−6+…+(−1)**(n+1)⋅n
# Note. Let's take a closer look at the 2nd test. For the number n=5 we will have the following sum: 1−2+3−4+5=3.


counter = 0 
n = int(input())
for i in range(1,n+1):
    if i%2==0:
        counter -= i
    else:
        counter += i
print(counter)


Sample Input 1:
1
Sample Output 1:
1
Sample Input 2:
5
Sample Output 2:
3
Sample Input 3:
3
Sample Output 3:
2

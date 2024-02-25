# All together 2
# A natural number is given. Write a program that calculates:
# - the number of digits is 3;
# - how many times the last digit appears in it;
# - number of even digits;
# - the sum of its digits greater than five;
# - the product of digits greater than seven (if there are no digits greater than seven, then output 1, if there is only one such digit, then output it);
# - how many times the numbers 0 and 5 appear in it (in total).
Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:
- количество цифр 3 в нем;
- сколько раз в нем встречается последняя цифра;
- количество четных цифр;
- сумму его цифр, больших пяти;
- произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
- сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).



n = int(input())
counter3 = 0  #количество цифр 3 в нем;
counterlast= 0 #сколько раз в нем встречается последняя цифра;
a = n % 10
counterh= 0 #количество четных цифр;
counter5 = 0 #сумму его цифр, больших пяти;
counter7 = 1 #произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
counter05 = 0 #сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
while n > 0:
    if n%10 == 3:
        counter3+=1
    if n%10 ==a:
        counterlast+=1
    if (n%10)%2 ==0:
        counterh+=1
    if n%10>5:
        counter5+=n%10
    if n%10>7:
        counter7*=n%10
    if n%10 == 0 or n%10 == 5:
        counter05+=1
    n=n//10
print(counter3)
print(counterlast)
print(counterh)
print(counter5)
print(counter7)
print(counter05)




Sample Input 1:
56639
Sample Output 1:
1
1
2
21
9
1
Sample Input 2:
56689932106
Sample Output 2:
1
3
6
44
648
2
Sample Input 3:
255
Sample Output 3:
0
2
1
0
1
2

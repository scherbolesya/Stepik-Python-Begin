# Three cities
# The names of three cities are given. Write a program that determines the shortest and longest name of a city.
# Note. It is guaranteed that the lengths of the names of all three cities are different.

# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# Примечание. Гарантируется, что длины названий всех трех городов различны.


a = input() #Три города
b = input()
c = input()
a1 = len(a)
b1 = len(b)
c1 = len(c)
if a1<b1 and a1<c1:
    print(a)
elif b1<a1 and b1<c1:
    print(b)
elif c1<a1 and c1<b1:
    print(c)
if a1>b1 and a1>c1:
    print(a)
elif b1>a1 and b1>c1:
    print(b)
elif c1>a1 and c1>b1:
    print(c)
  

Sample Input 1:
Москва
Санкт-Петербург
Екатеринбург
Sample Output 1:
Москва
Санкт-Петербург
Sample Input 2:
Нью-Йорк
Вашингтон
Чикаго
Sample Output 2:
Чикаго
Вашингтон
Sample Input 3:
Париж
Марсель
Лион
Sample Output 3:
Лион
Марсель

# 451 degrees Fahrenheit
# The famous American writer Ray Bradbury has a novel “Fahrenheit 451”. Write a program that determines what temperature on the Celsius scale corresponds to a given value on the Fahrenheit scale.

# 451 градус по Фаренгейту
# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». 
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

F = float(input()) # какой шкале Цельсия соответствует шкала Фаренгейта
C = 5/9*(F-32)
print(C)


Sample Input 1:
450.55
Sample Output 1:
232.5277777777778
Sample Input 2:
113.75
Sample Output 2:
45.41666666666667
Sample Input 3:
275.0
Sample Output 3:
135.0

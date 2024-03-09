Количество цифр
# Number of digits
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# A line of text is given as input to the program. Write a program that counts the number of digits in a given string.

n = input()
a = '1234567890'
b = 0
for i in range(len(n)):
    if n[i] in a:
        b+=1
print(b)


Sample Input 1:
nezabud dl-6
Sample Output 1:
1
Sample Input 2:
l33t 3301
Sample Output 2:
6

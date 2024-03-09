Нижний регистр
# lower case
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
# A string is given as input to the program. Write a program that counts the number of lowercase letter characters.

s=input() 
s1= 'abcdefghijklmnopqrstuvwxyz'
a=0
for i in range(len(s)):
    if s[i] in s1:
        a+=1
print(a)


Sample Input 1:
abcABCD12345
Sample Output 1:
3
Sample Input 2:
gggggggg1212321ABDCEFCE
Sample Output 2:
8
Sample Input 3:
2376423745dhdhdPPPP
Sample Output 3:
5

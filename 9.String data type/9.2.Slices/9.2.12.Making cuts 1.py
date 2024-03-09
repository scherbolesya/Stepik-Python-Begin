Делаем срезы 1
# Making cuts 1
На вход программе подается одна строка. Напишите программу, которая выводит:
1.общее количество символов в строке;
2.исходную строку, повторенную 3 раза;
3.первый символ строки;
4.первые три символа строки;
5.последние три символа строки;
6.строку в обратном порядке;
7.строку с удаленным первым и последним символом.
# One line is given as input to the program. Write a program that prints:
# 1.total number of characters in the line;
# 2.the original line repeated 3 times;
# 3.first character of the line;
# 4.the first three characters of the line;
# 5.last three characters of the line;
# 6.line in reverse order;
# 7.string with the first and last characters removed.

s = str(input())
s1 = len(s) #общее количество сabcdefghijklmnopqrstuvwxyz
s2=s+s+s #исходную строку повторенную 3 раза;
s3=s[:1] #первый символ строки;
s4=s[:3] #первые три символа строки;
s5=s[-3:] #последние три символа строки;
s6=s[::-1] #строку в обратном порядке;
s7=s[1:len(s)-1] #строку с удаленным первым и последним символом.
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

  
Sample Input:
abcdefghijklmnopqrstuvwxyz
Sample Output:
26
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
a
abc
xyz
zyxwvutsrqponmlkjihgfedcba
bcdefghijklmnopqrstuvwxy

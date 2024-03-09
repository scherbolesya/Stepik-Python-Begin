Делаем срезы 2
# Making cuts 2
На вход программе подается одна строка. Напишите программу, которая выводит:
1.третий символ этой строки;
2.предпоследний символ этой строки;
3.первые пять символов этой строки;
4.всю строку, кроме последних двух символов;
5.все символы с четными индексами;
6.все символы с нечетными индексами;
7.все символы в обратном порядке;
8.все символы строки через один в обратном порядке, начиная с последнего.
# One line is given as input to the program. Write a program that prints:
# 1.third character of this line;
# 2.penultimate character of this line;
# 3.the first five characters of this line;
# 4.the entire line except the last two characters;
# 5.all symbols with even indices;
# 6.all symbols with odd indices;
# 7.all characters in reverse order;
# 8.all characters of the line one after another in reverse order, starting from the last one.

  
s = input()
print(s[2:3], s[-2:-1], s[0:5], s[0:-2], s[0::2], s[1::2], s[::-1], s[::-2], sep='\n')

  
Sample Input:
abcdefghijklmnopqrstuvwxyz
Sample Output:
c
y
abcde
abcdefghijklmnopqrstuvwx
acegikmoqsuwy
bdfhjlnprtvxz
zyxwvutsrqponmlkjihgfedcba
zxvtrpnljhfdb

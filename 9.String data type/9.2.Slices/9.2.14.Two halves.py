Две половинки
# Two halves
На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.
Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.
# A line of text is given as input to the program. Write a program that will cut it into two equal parts, rearrange them and display them on the screen.
# Note. If the length of the string is odd, then the length of the first part must be one character longer.


s = input()
s1 = s[:len(s)//2+len(s)%2]
s2 = s[len(s)//2+len(s)%2:]
print(s2+s1)


Sample Input 1:
abcdef
Sample Output 1:
defabc
Sample Input 2:
abcdefg
Sample Output 2:
efgabcd
Sample Input 3:
a
Sample Output 3:
a

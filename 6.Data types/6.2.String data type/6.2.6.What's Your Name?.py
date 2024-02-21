# What's Your Name?
# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# Write a program that reads two lines from the keyboard - the user's first and last name and prints the phrase:
# «Hello [введенное имя] [введенная фамилия]! You have just delved into Python».
# Примечание. Между firstname lastname вставьте пробел =)
# Note. Insert a space between firstname lastname =)


f = input() #What's Your Name?
l = input()
h = 'Hello'
b = '! You just delved into Python'
print(h, f, l+b, sep=' ')


Sample Input 1:
Anthony
Joshua
Sample Output 1:
Hello Anthony Joshua! You have just delved into Python
Sample Input 2:
Michael
Jordan
Sample Output 2:
Hello Michael Jordan! You have just delved into Python
Sample Input 3:
Leonardo
DiCaprio
Sample Output 3:
Hello Leonardo DiCaprio! You have just delved into Python

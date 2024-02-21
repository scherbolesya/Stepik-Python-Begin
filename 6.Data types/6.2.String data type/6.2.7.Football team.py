# Football team
# Write a program that reads the name of a football team from the keyboard and prints the phrase:
# "Football team [entered string] has length [length of entered string] characters."

# Футбольная команда
# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».


k = input() #Футбольная команда
k1 = len(k)
f = 'Футбольная команда'
f1 ='имеет длину'
f2 = 'символов'
print(f,k,f1,k1,f2)


Sample Input 1:
Barcelona
Sample Output 1:
Футбольная команда Barcelona имеет длину 9 символов
Sample Input 2:
Real Madrid
Sample Output 2:
Футбольная команда Real Madrid имеет длину 11 символов
Sample Input 3:
Manchester United
Sample Output 3:
Футбольная команда Manchester United имеет длину 17 символов
Sample Input 4:
Milan
Sample Output 4:
Футбольная команда Milan имеет длину 5 символов

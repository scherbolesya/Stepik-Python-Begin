# Mood color blue
# Write a program that reads one line and then prints “YES” if the input line contains the substring “blue” and “NO” otherwise.
# Цвет настроения синий
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если во введенной строке есть подстрока «синий» и «NO» - в противном случае.


s = input() #Цвет настроения синий // ищет в предложении слово синий
s1 = 'синий'
if s1 in s:
    print('YES')
else:
    print('NO')
  

Sample Input 1:
Какой хороший день!
Sample Output 1:
NO
Sample Input 2:
Как называется этот красивый синий камень в Вашем кольце?
Sample Output 2:
YES
Sample Input 3:
Разглядите синий густой цвет.
Sample Output 3:
YES

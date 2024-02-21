# Are we resting?
# Write a program that reads one line and then prints “YES” if the input line contains the substring “Saturday” or “Sunday”, and “NO” otherwise.
# Отдыхаем ли?
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.


s = input() #Отдыхаем ли?
s1 = 'суббота'
s2 = 'воскресенье'
if s1 in s:
    print('YES')
elif s2 in s:
    print('YES')
else:
    print('NO')
  

Sample Input 1:
Какой сегодня день недели?
Sample Output 1:
NO
Sample Input 2:
Была суббота, и ему хотелось поскорее уехать домой.
Sample Output 2:
YES
Sample Input 3:
День в воскресенье выдался тёплым и солнечным.
Sample Output 3:
YES

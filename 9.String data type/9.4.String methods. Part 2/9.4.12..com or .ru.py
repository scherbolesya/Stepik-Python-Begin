.com or .ru
На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
# A line of text is given as input to the program. Write a program that checks that a string ends with the substring .com or .ru.

n = input()
if n.endswith('.ru') or n.endswith('.com'):
    print('YES')
else:
    print('NO')


Sample Input 1:
www.stepik.org
Sample Output 1:
NO
Sample Input 2:
www.google.com
Sample Output 2:
YES
Sample Input 3:
www.yandex.ru
Sample Output 3:
YES

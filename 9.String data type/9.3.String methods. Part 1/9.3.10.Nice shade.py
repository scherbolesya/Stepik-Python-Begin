Хороший оттенок
# Nice shade
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет. 
Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.
# A line of text is given as input to the program. Write a program that determines whether the shade of a text is good or not. 
# The text has a good connotation if it contains the substring “good” in all possible cases.
# Note. Text containing good, good, good, good, etc. has a good shade.

s=input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')


Sample Input 1:
я очень хороший текст =)
Sample Output 1:
YES
Sample Input 2:
оыралоывало ХОРОШвмсва выарлво83кг834
Sample Output 2:
YES
Sample Input 3:
Цвет настроения синий
Sample Output 3:
NO

Минутка генетики
# A minute of genetics
На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). 
Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
Примечание. Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.
# The input to the program is a string of genetic code consisting of the letters A (adenine), G (guanine), C (cytosine), T (thymine).
# Write a program that calculates how much adenine, guanine, cytosine and thymine are in a given line of genetic code.
# Note. The line does not contain characters other than A, G, C, T, a, g, c, t.

s = input() 
s1 = s.lower()
print('Аденин:', s1.count('а'))
print('Гуанин:', s1.count('г'))
print('Цитозин:', s1.count('ц'))
print('Тимин:', s1.count('т'))


Sample Input 1:
АааГГЦЦцТТттт
Sample Output 1:
Аденин: 3
Гуанин: 2
Цитозин: 3
Тимин: 5
Sample Input 2:
ааггццттААГГЦЦТТ
Sample Output 2:
Аденин: 4
Гуанин: 4
Цитозин: 4
Тимин: 4

Заглавные буквы
# Capital letters

На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом. 
Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
Примечание. Строка содержит только буквы.

# The input to the program is a string consisting of the person’s first and last name, separated by one space.
# Write a program that checks that the first and last names begin with a capital letter.
# Note. The string contains only letters.

s = input()
if s == s.title():
    print('YES')
else:
    print('NO')


Sample Input 1:
chris alan
Sample Output 1:
NO
Sample Input 2:
Chris Alan
Sample Output 2:
YES
Sample Input 3:
chris Alan
Sample Output 3:
NO

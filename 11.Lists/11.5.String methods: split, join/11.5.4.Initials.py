# Initials
# The input to the program is a line of text containing the person's first, middle and last names. Write a program that prints a person's initials.
Инициалы
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

s = input()
s1 = s.split()
s2 = []
for i in range(len(s1)):
    s2 += s1[i][0]
#s = '**'.join(chars)    
print('.'.join(s2), end='.')


Sample Input:
Владимир Семенович Высоцкий

Sample Output:
В.С.В.

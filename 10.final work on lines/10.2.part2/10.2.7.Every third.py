# Every third
# A line of text is given as input to the program. Write a program that removes from it all characters with indices divisible by 3, that is, characters with indices 0, 3, 6, ....
Каждый третий
На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с индексами, кратными 3, то есть символы с индексами 0, 3, 6, ....

s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)


Sample Input:
Python
Sample Output:
yton

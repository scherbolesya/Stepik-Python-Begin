Замени меня полностью
На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».
# Replace me completely
# A line of text is given as input to the program. Write a program that replaces all occurrences of the number 1 with the word "one".

s = str(input()) #
a = ''
for i in s:
    if i == '1':
        print('one', end='')
    else:
        print(i, end='')
      
  
Sample Input:
1231
Sample Output:
one23one

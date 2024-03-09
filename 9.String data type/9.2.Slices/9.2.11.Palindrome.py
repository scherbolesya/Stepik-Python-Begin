# Palindrome
# The input to the program is one word, written in lower case. Write a program that determines whether it is a palindrome.
# Note. A palindrome is a word that reads the same in both directions. For example, the word "flood" is a palindrome.
Палиндром
На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет, является ли оно палиндромом.
Примечание. Палиндром считается слово, которое читается одинаково в обоих направлениях. Например, слово «потоп» является палиндромом.

s=input()
if s[:]==s[::-1]:
    print('YES')
else:
    print('NO')
  
  
Sample Input 1:
потоп
Sample Output 1:
YES
Sample Input 2:
анекдот
Sample Output 2:
NO

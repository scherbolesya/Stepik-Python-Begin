Удаление фрагмента
# Deleting a fragment
На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, 
которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
# The input to the program is a line of text in which the letter “h” appears at least twice. Write a program
# which removes the first and last occurrence of the letter "h" from this string, as well as all characters between them.

s = input() 
print(s[:s.find('h')]+s[s.rfind('h')+1:])


Sample Input 1:
ahahahahaha
Sample Output 1:
aa
Sample Input 2:
hh
Sample Output 2:

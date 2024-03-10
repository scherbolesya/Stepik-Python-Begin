# Valid number 🌶️🌶️
Валидный номер 🌶️🌶️
На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером. 
Строка текста является корректным телефонным номером, если она имеет формат: abc-def-hijk или 7-abc-def-hijk,
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть правильным.
# На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером. 
# Строка текста является корректным телефонным номером, если она имеет формат: abc-def-hijk или 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть правильным.

n = input().split('-')
a = n
if ''.join(a).isdigit() == True:
    if int(n[0]) == 7:
        n.remove(n[0]) 
    if len(list(n[0])) == 3 and len(list(n[1])) == 3 and len(list(n[2])) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
  
  
Sample Input 1:
7-301-447-5820
Sample Output 1:
YES
Sample Input 2:
301-447-5820
Sample Output 2:
YES
Sample Input 3:
301-4477-5820
Sample Output 3:
NO
Sample Input 4:
3X1-447-5820
Sample Output 4:
NO
Sample Input 5:
3014475820
Sample Output 5:
NO

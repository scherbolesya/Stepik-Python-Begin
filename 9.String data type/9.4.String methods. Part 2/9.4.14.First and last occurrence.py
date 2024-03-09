Первое и последнее вхождение
# First and last occurrence
На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. 
Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной строке, разделенные символом пробела. 
Если буква «f» в данной строке не встречается, следует вывести «NO».
# A line of text is given as input to the program. If the letter “f” appears only once in this line, print its index.
# If it occurs two or more times, print the indices of its first and last occurrence on the same line, separated by a space character.
# If the letter "f" does not appear in this line, "NO" should be printed.

s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
  

Sample Input 1:
abcdefg
Sample Output 1:
5
Sample Input 2:
abcdefgfhfabc
Sample Output 2:
5 9
Sample Input 3:
abcd
Sample Output 3:
NO

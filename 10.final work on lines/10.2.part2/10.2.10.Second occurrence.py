Второе вхождение
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». 
Если буква «f» встречается только один раз, выведите число −1, а если не встречается ни разу, выведите число −2.
# Second occurrence
# A line of text is given as input to the program. Write a program that prints the index of the second occurrence of the letter "f".
# If the letter “f” appears only once, print the number −1, and if it does not appear even once, print the number −2.

s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
  
  
Sample Input 1:
affective
Sample Output 1:
2
Sample Input 2:
python
Sample Output 2:
-2
Sample Input 3:
father
Sample Output 3:
-1

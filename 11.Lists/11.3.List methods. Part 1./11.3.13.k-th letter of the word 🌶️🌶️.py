# k-th letter of the word 🌶️🌶️
# The input to the program is a natural number n and n strings, and then the number k. Write a program that prints the kth letter from the input strings
# on one line without spaces.
# Note. If some lines are too short and do not contain a character with a given number, then such lines should be ignored in output.
k-ая буква слова 🌶️🌶️
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую букву из введенных строк 
на одной строке без пробелов.
Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.

n = int(input())
abc = []
for i in range(n):
    abc.append(input())
k = int(input()) - 1
for j in range(len(abc)):
    if len(abc[j])>= k+1:
               print(abc[j][k], end='')
    else:
        continue
      

Sample Input:
5
abcdef
bcdefg
cdefgh
defghi
efghij
2
Sample Output:
bcdef

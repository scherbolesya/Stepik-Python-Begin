# Till the end 2
До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или 
«конец» (большими или маленькими буквами, без кавычек). При этом сами слова «КОНЕЦ» и «конец» не входят в последовательность, 
лишь символизируя её окончание. Напишите программу, которая выводит члены данной последовательности.
# The input to the program is a sequence of words, each word on a separate line. The end of the sequence is the word "END" or
# “end” (in capital or small letters, without quotes). Moreover, the words “END” and “end” themselves are not included in the sequence,
# only symbolizing its end. Write a program that prints the members of a given sequence.

  
text = input()
while (text != 'КОНЕЦ') and (text != 'конец'):
    print(text)
    text = input()


Sample Input 1:
JavaScript
C++
C#
Ruby
PHP
КОНЕЦ
Python
Sample Output 1:
JavaScript
C++
C#
Ruby
PHP
Sample Input 2:
Великобритания
США
Китай
КОНЕЦ
Ватикан
Sample Output 2:
Великобритания
США
Китай
Sample Input 3:
for
while
конец
for while
Sample Output 3:
for
while

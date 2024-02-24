# Till the end 1
До КОНЦА 1
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). 
При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание. Напишите программу, 
которая выводит члены данной последовательности.
# The input to the program is a sequence of words, each word on a separate line. The end of the sequence is the word “END” (without quotes).
# Moreover, the word “END” itself is not included in the sequence, only symbolizing its end. Write a program
# which outputs the members of a given sequence.

  
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()
  
  
Sample Input 1:
Fus
Ro
КОНЕЦ
Dah
Sample Output 1:
Fus
Ro
Sample Input 2:
П
небу
полуночи
КОНЕЦ
ангел
летел
Sample Output 2:
По
небу
полуночи
Sample Input 3:
Dead
by
Daylight
КОНЕЦ
Good Game
Sample Output 3:
Dead
by
Daylight  

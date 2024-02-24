# Number of members
Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: 
«стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Сами эти слова в последовательность не входят, лишь символизируя её окончание. 
Напишите программу, которая выводит общее количество членов данной последовательности.
# The input to the program is a sequence of words, each word on a separate line. The end of the sequence is one of three words:
# “stop”, “enough”, “enough” (in small letters, without quotes). These words themselves are not included in the sequence, only symbolizing its ending.
# Write a program that prints the total number of terms of a given sequence.


a =  input()
total = 0
while a not in ('стоп', 'хватит', 'достаточно'):
    total += 1
    a = input()
print(total)


Sample Input 1:
Skyrim
GTA
Mafia
стоп
Battlefield
Sample Output 1:
3
Sample Input 2:
Yandex
Google
Opera
Safari
хватит
Mozilla
Sample Output 2:
4
Sample Input 3:
Skype
Viber
Telegram
WhatsApp
Discord
достаточно
Sample Output 3:
5

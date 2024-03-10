# Youth slang
Молодежный жаргон
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу: 
1.первая буква каждого слова удаляется и ставится в конец слова; 
2.затем в конец слова добавляется слог "ки".
# A line of text is given as input to the program. Write a program using a list expression that converts each word of the input text into "teen slang" according to the following rule:
# 1. the first letter of each word is removed and placed at the end of the word;
# 2.then the syllable “ki” is added to the end of the word.

t = input()
n = ' '.join(word[1:] + word[0] + 'ки' for word in t.split())
print(n)


Sample Input:
проспал почти всю ночь
Sample Output:
роспалпки очтипки сювки очьнки

Количество артиклей
# Number of articles
На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
# The input to the program is a string containing English text. Write a program that counts the total number of articles: 'a', 'an', 'the'.
# Note. Articles may begin with a capital letter 'A', 'An', 'The'.

a = input().lower().split()
print('Общее количество артиклей:', a.count('a')+a.count('an')+a.count('the'))


Sample Input:
William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, 
where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. 
In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.

Sample Output:
Общее количество артиклей: 7

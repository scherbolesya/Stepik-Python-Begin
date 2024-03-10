# The longest
Самый длинный
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.
# A line of text is given as input to the program. Write a program using a list expression that finds the length of the longest word.

a = [len(i) for i in input().split()]
print(max(a))


Sample Input:
проспал почти всю ночь
Sample Output:
7

# Characters of all lines
# The input to the program is a natural number n, and then n strings. Write a program that creates a list of characters from all strings and then prints it.
# Note. The resulting list may contain identical characters.
Символы всех строк
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.
Примечание. В результирующем списке могут содержаться одинаковые символы.

n = int(input())
a = []
for i in range(n):
    s = input()
    a.extend(s)
print(a)

  
Sample Input:
3
abc
def
ghi
Sample Output:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

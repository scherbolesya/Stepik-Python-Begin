# Same neighbors
Одинаковые соседи
На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
# One line is given as input to the program. Write a program that determines how many identical adjacent symbols it contains.

n = input() 
a=n
counter = 0
for i in range(len(n)-1):
    if n[i] == a[i+1]:
        counter+=1
print(counter)


Sample Input 1:
abcd
Sample Output 1:
0
Sample Input 2:
aabbcc
Sample Output 2:
3
Sample Input 3:
aaa
Sample Output 3:
2

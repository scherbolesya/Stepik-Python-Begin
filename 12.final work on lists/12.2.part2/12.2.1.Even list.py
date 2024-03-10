# Even list
Список четных
На вход программе подается четное число n,n≥2. Напишите программу, которая выводит список четных чисел [2, 4, 6, ..., n].
# An even number n,n≥2 is given as input to the program. Write a program that prints a list of even numbers [2, 4, 6, ..., n].

numbers = list(range(2, int(input())+1, 2))
#for i in numbers:
  #  print(i, end='*')
print(numbers)


Sample Input 1:
2
Sample Output 1:
[2]
Sample Input 2:
4
Sample Output 2:
[2, 4]
Sample Input 3:
8
Sample Output 3:
[2, 4, 6, 8]

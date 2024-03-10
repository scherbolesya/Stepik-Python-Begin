# List expression 1
Списочное выражение 1
На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, которая создает список, 
содержащий квадраты чисел от 1 до n (включительно), а затем выводит его элементы построчно, то есть каждый на отдельной строке.
Примечание. Для вывода элементов списка используйте цикл for.
# The program input is a natural number n. Write a program using a list expression that produces a list,
# containing the squares of numbers from 1 to n (inclusive), and then displays its elements line by line, that is, each on a separate line.
# Note. To display the elements of a list, use a for loop.

p = [i**2 for i in range(1, int(input())+1)]
print(*p, sep="\n")


Sample Input:
5
Sample Output:
1
4
9
16
25

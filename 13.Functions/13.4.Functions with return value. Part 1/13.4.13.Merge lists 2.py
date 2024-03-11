# Merge lists 2
На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
# The number is given as input to the program n and then n lines containing integers in ascending order. Lists of numbers are formed from these lines. Write a program that merges the given lists into one sorted list using the quick_merge() function and then outputs it.

  
def quick_merge(list1):
    b = []
    for i in range(list1):
        a = [int(c) for c in input().split()]
        b.extend(a)
    b.sort()
    return b
n = int(input())
print(*quick_merge(n))


Sample Input 1:
3
1 2 3 4
5 6 7
10 11 17
Sample Output 1:
1 2 3 4 5 6 7 10 11 17
Sample Input 2:
4
10 20
1 15
5 17
8 13 19
Sample Output 2:
1 5 8 10 13 15 17 19 20

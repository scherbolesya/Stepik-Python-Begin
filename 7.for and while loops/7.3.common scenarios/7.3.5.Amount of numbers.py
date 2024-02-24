# Amount of numbers
# Количество чисел
На вход программе подаются два целых числа a и b(a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b (включительно), 
куб которых оканчивается на 4 или 9.
Примечание. Куб числа a – это его третья степень (a 3).


counter = 0
a = int(input())
b = int(input())
for i in range(a, b+1):
    if (i**3)%10 == 4 or (i**3)%10 == 9:
        counter = counter + 1
print(counter)


Sample Input 1:
1
10
Sample Output 1:
2
Sample Input 2:
1
100
Sample Output 2:
20
Sample Input 3:
10
1786
Sample Output 3:
355

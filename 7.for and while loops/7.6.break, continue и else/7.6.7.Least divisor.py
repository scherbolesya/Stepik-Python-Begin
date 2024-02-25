# Least divisor
# The number n>1 is given as input to the program. Write a program that prints its smallest non-1 divisor.
# Note. Use the break statement when encountering a divisor.
Наименьший делитель
На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
Примечание. Используйте оператор break при обнаружении делителя.


num = int(input())  #Наименьший делитель Программа должна вывести наименьший делитель отличный от 11.
for i in range(2,num+1):
    if num % i == 0:
        print(i)
        break
    else:
        num % i !=0
        continue


Sample Input 1:
15
Sample Output 1:
3
Sample Input 2:
17
Sample Output 2:
17
Sample Input 3:
67834658736534870
Sample Output 3:
2

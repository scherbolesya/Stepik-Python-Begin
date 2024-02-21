# На вход программе подается число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах по следующему алгоритму: 
# в течение первых двух лет собачий год равен 10.5 человеческим годам, после этого каждый год собаки равен 4 человеческим годам.

# The input to the program is the number n - the number of dog years. Write a program that calculates the age of a dog in human years using the following algorithm: 
# for the first two years, a dog year is equal to 10.5 human years, after that each dog year is equal to 4 human years.

n = int(input()) # вычисляет  возраст собаки в человеческих годах
if n <= 2:
    print(n*10.5)
elif n > 2:
    print(21 + ((n-2)*4))


Sample Input 1:
1
Sample Output 1:
10.5
Sample Input 2:
2
Sample Output 2:
21
Sample Input 3:
3
Sample Output 3:
25

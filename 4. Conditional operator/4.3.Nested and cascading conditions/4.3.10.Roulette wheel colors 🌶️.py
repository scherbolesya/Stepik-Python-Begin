# Roulette wheel colors 🌶️
# On the roulette wheel, the pockets are numbered from 0 to 36. Below are the colors of the pockets:
# pocket 0 green;
# for pockets 1 to 10, pockets with an odd number are red, pockets with an even number are black;
# for pockets 11 to 18, pockets with an odd number are black, pockets with an even number are red;
# for pockets 19 to 28, pockets with an odd number are red, pockets with an even number are black;
# for pockets 29 to 36, odd-numbered pockets are black, even-numbered pockets are red.
# Write a program that reads a pocket number and shows whether the pocket is green, red or black. 
# The program should display an error message if the user enters a number that is outside the range from 0 to 36.


# Цвета колеса рулетки 🌶️
# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: 
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. 
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

a = int(input())
if a == 0:
    print('зеленый')
elif 1<=a<=10 and a%2==0:
    print('черный')
elif 1<=a<=10 and a%2 != 0:
    print('красный')
elif 11<=a<=18 and a%2==0:
    print('красный')
elif 11<=a<=18 and a%2 !=0:
    print('черный')
elif 19<=a<=28 and a%2==0:
    print('черный')
elif 19<=a<=28 and a%2 !=0:
    print('красный')
elif 29<=a<=36 and a%2==0:
    print('красный')
elif 29<=a<=36 and a%2 !=0:
    print('черный')
else:
    print('ошибка ввода')

# Sample Input 1:
# 0
# Sample Output 1:
# зеленый
# Sample Input 2:
# 1
# Sample Output 2:
# красный
# Sample Input 3:
# 37
# Sample Output 3:
# ошибка ввода

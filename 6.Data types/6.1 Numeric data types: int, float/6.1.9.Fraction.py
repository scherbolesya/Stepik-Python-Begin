# Fraction
# A positive real number is given. Print its fractional part.
# Note. Floating-point numbers (float type) in Python are stored in an imprecise form, which is due to the limited number of bytes allocated for them in memory. 
# Therefore, your program may produce the fractional part of a number in a way that is not expected. For example, for the number 44.45 the remainder might look like:
0.45000000000000284
# Our checking system will count both 0.45 and 0.45000000000000284 as correct answers.

# Дробная часть
# Дано положительное действительное число. Выведите его дробную часть.
# Примечание. Числа с плавающей точкой (тип float) в Python хранятся в неточном виде, что связано с ограниченным количеством выделенных для них байт в памяти. 
# Поэтому ваша программа может выдавать дробную часть от числа не в ожидаемом виде. Например, для числа 44.45 остаток может выглядеть как:
0.45000000000000284
# Наша проверяющая система засчитает как 0.45, так и 0.45000000000000284 правильными ответами.

a = float(input()) #дробная часть программа должна вывести дробную часть числа 0,15
b = a - int(a)
print(b)


Sample Input 1:
44.45
Sample Output 1:
0.45
Sample Input 2:
39483.2
Sample Output 2:
0.2
Sample Input 3:
322.4958
Sample Output 3:
0.4958

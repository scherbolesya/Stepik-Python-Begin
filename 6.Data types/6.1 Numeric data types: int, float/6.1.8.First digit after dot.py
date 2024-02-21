# First digit after dot
# A positive real number is given. Print its first digit after the decimal point.

# Первая цифра после точки
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

a = float(input()) #первая цифра после точки
b = ((a*10)%10)
print(int(b))


Sample Input 1:
3384390.4339
Sample Output 1:
4
Sample Input 2:
1.5
Sample Output 2:
5
Sample Input 3:
459933200.23
Sample Output 3:
2

# Absolute amount
# Given five numbers a1, a2, a3, a4, a5. Write a program that calculates the sum of their moduli ∣a1∣+∣a2∣+∣a3∣+∣a4∣+∣a5∣.

# Абсолютная сумма
# Даны пять чисел a1, a2, a3, a4, a5 . Напишите программу, которая вычисляет сумму их модулей ∣a1∣+∣a2∣+∣a3∣+∣a4∣+∣a5∣.

a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
print(abs(a1)+abs(a2)+abs(a3)+abs(a4)+abs(a5))


Sample Input 1:
5.4
33
-1232
-3.889
6
Sample Output 1:
1280.289
Sample Input 2:
0
-776.4
0
343
55.24
Sample Output 2:
1174.64
Sample Input 3:
-5.4643234
0
223
5
7
Sample Output 3:
240.4643234

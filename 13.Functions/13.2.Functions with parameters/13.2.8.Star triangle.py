# Star triangle
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
1.fill – символ заполнитель;
2.base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
# Write a function draw_triangle(fill, base) that takes two parameters:
# 1.fill – filler symbol;
# 2.base – the size of the base of an isosceles triangle;
# and then takes it out.
# Note. It is guaranteed that the base of the triangle is an odd number.

def draw_triangle(fill, base):
    n = base//2
    i = 0
    for i in range(1,n+2):    
        print(fill *i)
        i +=1
        
    k = i-1
    for j in range(1,n+1):
        k -= 1
        print(fill *k)
        # считываем данные
fill = input()
base = int(input())
# вызываем функцию
draw_triangle(fill, base)


Sample Input 1:
*
9
Sample Output 1:
*
**
***
****
*****
****
***
**
*
Sample Input 2:
+
5
Sample Output 2:
+
++
+++
++
+
Sample Input 3:
?
7
Sample Output 3:
?
??
???
????
???
??
?

Звездный треугольник 1
# Star triangle 1
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в соответствии с образцом:
# Write a function draw_triangle() that draws a star-shaped right triangle with legs equal to 10 as shown:
*
**
***
****
*****
******
*******
********
*********
**********
Примечание. Для вывода треугольника используйте цикл for.
# Note. To draw a triangle, use a for loop.

# объявление функции
def draw_triangle():
    for i in range(1,11):
        print('*'*i)

# основная программа
draw_triangle()  # вызов функции

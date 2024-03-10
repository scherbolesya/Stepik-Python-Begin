# Star rectangle 1
Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
# Write a function draw_box() that draws a 14x10 star rectangle as shown:
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
Примечание. Для вывода прямоугольника используйте цикл for. 
# Note. Use a for loop to draw a rectangle.

# объявление функции
def draw_box():
    for i in range(14):
        if i == 0:
            print('*'*10)
        elif i == 13:
            print('*'*10)
        else:
            print('*',' '*8,'*', sep='')
# основная программа
draw_box()  # вызов функции

# Dividers 2
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
Примечание 2. Следующий программный код:
# Write a function number_of_factors(num) that takes a number as an argument and returns the number of factors of that number.
# Note 1: Use the already implemented get_factors(num) function from the previous task.
# Note 2: The following program code:
print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))

должен выводить:
# should output:
1
2
4



# объявление функции
def get_factors(num):
    a = 0
    for i in range(1, num+1):
        if num % i == 0:
            a +=1
    return a
# считываем данные
n = int(input())
# вызываем функцию
print(get_factors(n))




Номер теста  Входные данные  Выходные данные    
  1	          1	                1
  2	          5	                2
  3	          10	              4
  4	          36	              9
  5	          360	              24
  6	          10800	            60
  7	          101	               2

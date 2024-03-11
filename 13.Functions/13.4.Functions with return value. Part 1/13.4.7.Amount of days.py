# Amount of days
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
Примечание 2. Считайте, что год является невисокосным.
Примечание 3. Следующий программный код:
# Write a function get_days(month) that takes a month number as an argument and returns the number of days in a given month.
# Note 1: It is guaranteed that the argument passed is in the range from 1 to 12.
# Note 2: Consider the year to be a non-leap year.
# Note 3: The following program code:
print(get_days(1))
print(get_days(2))
print(get_days(9))

должен выводить:
# should output:
31
28
30



# объявление функции
def get_days(month):
    a = [31,28,31,30,31,30,31,31,30,31,30,31]
    return a[month-1]
# считываем данные
num = int(input())
# вызываем функцию
print(get_days(num))



Номер теста   Входные данные   Выходные данные    
    1	              1	            31
    2	              2	            28
    3	              3	            31
    4	              4	            30
    5	              5	            31
    6	              6	            30
    7	              7	            31
    8	              8	            31
    9	              9	            30
    10	            10	          31
    11	            11	          30
    12	            12	          31

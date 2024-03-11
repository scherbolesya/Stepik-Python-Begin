# Kilometer converter
Конвертер километров
Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. 
Формула для преобразования: мили = километры * 0.6214.
Примечание. Следующий программный код:
# Write a function convert_to_miles(km) that takes a distance in kilometers as an argument and returns the distance in miles.
# Formula for conversion: miles = kilometers * 0.6214.
# Note. The following program code:
print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))

должен выводить:
# should output:
0.6214
3.107
6.214



# объявление функции
def convert_to_miles(km):
    return '{:g}'.format(km * 0.6214)  
# считываем данные
num = int(input())
# вызываем функцию
print(convert_to_miles(num))



Тестовые данные 🟢
Номер теста   Входные данные    Выходные данные    
      1	        1	                0.6214
      2	        10	              6.214
      3	        5	                3.107
      4	        1000	            621.4

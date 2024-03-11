Тема урока: функции с возвратом значения

1.Функции с возвратом значения
2.Решение задач
Аннотация. Кроме функций, возвращающих числовые значения, можно писать и возвращающие логические, строковые и другие значения.

-----------------------------------------------------------------------------------------------------------------------------
  Возвращение булевых значений

Python позволяет писать булевы функции, возвращающие либо истину (True), либо ложь (False). Булеву функцию можно применять для проверки условия, тогда значения True и False будут сигнализировать о его выполнении.
Булевы функции широко применяются для упрощения сложных условий, проверяемых в структурах принятия решения и структурах с повторением.
Например, напишем программу, которая просит пользователя ввести число и определяет, четное оно или нечетное.

Это можно сделать так:
number = int(input())
if number % 2 == 0:
    print('Это число четное. ')
else:
    print('Это число нечетное.')

Этот фрагмент кода будет легче понять, если написать булеву функцию is_even(), которая принимает число в качестве аргумента и возвращает True, если оно четное, и False если нечетное.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

Теперь можно переписать инструкцию if-else основной программы так, чтобы она для определения четности переменной number вызывала функцию is_even():
number = int(input())
if is_even(number):
    print('Это число четное. ')
else:
    print('Это число нечетное.')

Так логику программы легче понять, а функцию можно вызывать в программе всякий раз, когда необходимо проверить четность числа.

----------------------------------------------------------------------------------------------------------------------------------
  Использование булевых функций для валидации входных данных

Булевы функции можно также использовать для упрощения сложного кода валидации входных данных. Например в программе, предлагающей пользователю ввести номер модели изделия, где возможны только значения 100, 200 или 300, можем написать такой код:
model = int(input())
while model != 100 and model != 200 and model != 300:
    print('Допустимыми номерами моделей являются 100, 200 или 300.')
    model = int(input())

Цикл валидации использует длинное составное булево выражение, и повторяется до тех пор, пока model не будет равняться 100, 200 или 300. 
Вместе с тем, цикл валидации можно упростить, написав булеву функцию проверки переменной model и вызывая ее в цикле. Напишем функцию is_invalid(), которая принимает один параметр model и возвращает значение True, если модель недопустима и False в противном случае. Тогда цикл валидации можно переписать следующим образом:
while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())

После этого изменения цикл становится легче читать. Теперь вполне очевидно, что цикл повторяется до тех пор, пока номер модели недопустим. Приведенный ниже фрагмент кода показывает, как можно было бы написать функцию is_invalid(). Она принимает номер модели в качестве аргумента, и если аргумент не равен 100, 200 или 300, то эта функция возвращает True, говоря, что он недопустимый. В противном случае функция возвращает False.
def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False
Создание функций, реализующих такую простую логику, — не всегда оптимальное решение, так как увеличивает размер кода и ведет к затратам времени на вызов функции и возврат обратно результата, что может сказаться негативно на производительности программы.

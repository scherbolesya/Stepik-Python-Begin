# Full name
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
1.name – имя человека;
2.surname – фамилия человека;
3.patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
# Write a function print_fio(name, surname, patronymic) that takes three parameters:
# 1.name – person’s name;
# 2.surname – person’s last name;
# 3.patronymic – patronymic of a person;
# and then prints the person’s full name.
# Note. Consider the fact that all three letters in the full name must be upper case.

# объявление функции
def print_fio(name, surname, patronymic):
    print(surname.upper()[0] + name.upper()[0] + patronymic.upper()[0])
# считываем данные
name, surname, patronymic = input(), input(), input()
# вызываем функцию
print_fio(name, surname, patronymic)

  
Sample Input 1:
Александр
Пушкин
Сергеевич
Sample Output 1:
ПАС
Sample Input 2:
тимур
Гуев
ахсарбекович
Sample Output 2:
ГТА

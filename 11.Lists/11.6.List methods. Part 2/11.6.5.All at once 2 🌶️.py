# All at once 2 🌶️
Все сразу 2 🌶️
Дополните приведенный код, чтобы он:
1.Заменил второй элемент списка на 17;
2.Добавил числа 4, 5 и 6 в конец списка;
3.Удалил первый элемент списка;
4.Удвоил список;
5.Вставил число 25 по индексу 3;
6.Вывел список, с помощью функции print()

Complete the given code so that it:
1. Replaced the second element of the list with 17;
2.Added numbers 4, 5 and 6 to the end of the list;
3.Deleted the first element of the list;
4.Doubled the list;
5.Inserted the number 25 at index 3;
6. Output a list using the print() function


numbers = [8, 9, 10, 11]
a = numbers.pop(1)    #Заменил второй элемент списка на 17;
numbers.insert(1, 17)
numbers.append(4) #Добавил числа 4, 5 и 6 в конец списка;
numbers.append(5)
numbers.append(6)
numbers.remove(8)#Удалил первый элемент списка;
numbers=numbers+numbers#Удвоил список;
numbers.insert(3, 25)#Вставил число 25 по индексу 3;
print(numbers)

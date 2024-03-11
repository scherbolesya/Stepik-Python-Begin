# Find everyone
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. 
Проблема заключается в том, что данный метод не находит местоположение всех символов а.
Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol 
и возвращает список, содержащий все местоположения этого символа в строке.
Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
Примечание 2. Следующий программный код:
# Recall that the string find('a') method returns the location of the first occurrence of the character a in the string.
# The problem is that this method does not find the location of all a's.
# Write a function called find_all(target, symbol) that takes two arguments: the string target and the symbol symbol
# and returns a list containing all locations of that character in the string.
# Note 1: If the specified character does not occur in the string, then an empty list should be returned.
# Note 2: The following program code:
print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))

должен выводить:
# should output:
[0, 4, 7, 8, 9]
[]
[4]



def find_all(target, symbol):
    return [i for i in range(0, len(s)) if target[i] == symbol]
# считываем данные
s = input()
char = input()
# вызываем функцию
print(find_all(s, char))



 Номер теста   Входные данные   Выходные данные    
    1	            abcdabcaaa
                      a	        [0, 4, 7, 8, 9]

    2	            abcadbcaaa
                      e	          []

    3	            abcadbcaaa
                      d	          [4]

    4	              tttt
                      t	          [0, 1, 2, 3]

    5	              ppooooopp
                        p	         [0, 1, 7, 8]

    6	              ppooooopp
                        o	          [2, 3, 4, 5, 6]

    7	              ppooppoopp
                        o	          [2, 3, 6, 7]

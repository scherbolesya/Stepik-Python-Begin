Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
Примечание 1. Списки list1 и list2 могут иметь разную длину.
Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.
Примечание 3. Следующий программный код:
  # Write a function merge(list1, list2) that takes two ascending-sorted integer lists as arguments and merges them into one sorted list.
# Note 1: The lists list1 and list2 may have different lengths.
# Note 2. You can use the sort() list method, or you can do without it 😎.
# Note 3: The following program code:
print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))

должен выводить:
# should output:
[1, 2, 3, 5, 6, 7, 8]
[1, 5, 6, 7, 10, 13, 16, 20]


  
def merge(list1, list2):
    list3 = list1 + list2 
    list3.sort()
    return(list3)
# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
# вызываем функцию
print(merge(numbers1, numbers2))

  
  
 Номер теста   Входные данные  Выходные данные    
    1	          1 2 3
                5 6 7 8	        [1, 2, 3, 5, 6, 7, 8]

    2	          1 7 10 16
                5 6 13 20	      [1, 5, 6, 7, 10, 13, 16, 20]

    3	          1
                2	              [1, 2]

    4	          1 2
                1 3	            [1, 1, 2, 3]

    5	          10 11 12
                1 2 3	          [1, 2, 3, 10, 11, 12]

Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
# Complete the code below so that it prints the sum of the squares of the elements in the numbers list.

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
a = 0
for i in range(len(numbers)):
    s = numbers[i]**2
    a+=s
print(a)

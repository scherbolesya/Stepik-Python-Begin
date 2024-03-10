Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).
Примечание. Результирующий список должен состоять из целых чисел.
# Complete the following code using a list expression to obtain a list of all palindromic numbers from 100 to 1000 (inclusive).
# Note. The resulting list must consist of integers.

palindromes = [i for i in range(100, 1000) if i % 10 == i // 100]
print(palindromes)

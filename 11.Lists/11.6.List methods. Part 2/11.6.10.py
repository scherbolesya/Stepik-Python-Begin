Что будет выведено в результате выполнения следующего программного кода? 
# What will be the output as a result of executing the following code?

numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
numbers.sort()
del numbers[0]
del numbers[-1]
numbers.sort(reverse=True)
print(numbers)

# [10, 8, 6, 5, 4, 4, 3, 2, 1]

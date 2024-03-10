С помощью функции list() можно из строки получить список ее символов, а с помощью функции join() можно склеить элементы списка, вставляя между ними разделитель.
Что будет выведено в результате выполнения следующего программного кода? 
# Using the list() function, you can get a list of its characters from a string, and using the join() function, you can glue list elements together by inserting a separator between them.
# What will be the output as a result of executing the following code?

s = 'BEEGEEK'
chars = list(s)
s = '**'.join(chars)
print(s)

# B**E**E**G**E**E**K

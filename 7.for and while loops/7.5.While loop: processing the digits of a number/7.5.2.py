Что покажет приведенный ниже фрагмент кода?
# What will the code snippet below show?
num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)
# 120

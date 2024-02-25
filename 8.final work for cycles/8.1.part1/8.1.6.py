# Determine what problem the following code fragment solves:
Определите какую задачу решает следующий фрагмент кода:

n = int(input())
counter = 0

for i in range(1, n + 1):
    if i % 3 == 0 and i % 7 != 0:    
        counter += 1
print(counter)

# выводит количество чисел от 1 до n кратных 3, но не кратных 7

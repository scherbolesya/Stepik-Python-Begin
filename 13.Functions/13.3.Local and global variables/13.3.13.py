Что покажет приведенная ниже программа?
#  What will the program below show?

x = 5
def add():
    global x
    x = 3
    x = x + 5
    print(x)
add()
print(x)

# 8
# 8

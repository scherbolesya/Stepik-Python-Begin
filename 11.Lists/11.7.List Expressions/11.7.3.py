Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного списка, где у каждой строки удалён первый символ.
# Complete the following code using a list expression to produce a new list containing the lines of the original list, with the first character removed from each line.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1:] for m in keywords]
print(new_keywords)

Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.
# Complete the following code using a list expression to produce a new list containing the lengths of the strings in the original list.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

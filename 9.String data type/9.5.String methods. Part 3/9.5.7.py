Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он вывел текст: 
«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
# Complete the given code using string formatting using the format method so that it outputs the text:
# “In 2010, someone paid 10k Bitcoin for two pizzas.” (without quotes).

s1 = 2010
s2 = '10k'
s3 = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(s1, s2 , s3)
print(s)

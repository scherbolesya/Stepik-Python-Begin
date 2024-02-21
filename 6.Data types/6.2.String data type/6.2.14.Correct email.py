# Correct email
# We will consider an email address to be correct if it contains a dog symbol (@) and a period (.). Write a program that checks the validity of an email address.
# Note. For real email addresses, the presence of the @ and . symbols is not enough, but their absence is guaranteed to result in an incorrect email.

# Корректный email
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки (.). Напишите программу, проверяющую корректность email адреса.
# Примечание. Для настоящих email адресов недостаточно наличия символов @ и ., однако их отсутствие гарантировано влечет за собой неверный email.


a = input()   #Корректный email
if '.' in a and '@' in a:
    print('YES')
else:
    print('NO')
  

Sample Input 1:
aaaa@bbb.com
Sample Output 1:
YES
Sample Input 2:
aaaa@bbbcom
Sample Output 2:
NO
Sample Input 3:
qwerty.com
Sample Output 3:
NO

Цифра 2
# Digit 2
На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру. 
В противном случае вывести сообщение «Цифр нет» (без кавычек).
# One line is given as input to the program. Write a program that prints the message "Number" (without quotes) if a string contains a number. 
# Otherwise, display the message “No numbers” (without quotes).

n = input()
a = '0123456789'
b = 0
for i in range(len(n)):
    if n[i] in a:
        b +=1
if b > 0:
    print('Цифра')    
else:       
    print('Цифр нет')
  

Sample Input 1:
Hi Python
Sample Output 1:
Цифр нет
Sample Input 2:
Hi 17 Python
Sample Output 2:
Цифра

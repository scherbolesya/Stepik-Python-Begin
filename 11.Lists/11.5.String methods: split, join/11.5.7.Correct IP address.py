Корректный ip-адрес
# Correct IP address
На вход программе подается строка текста, содержащая 4 целых неотрицательных числа, разделенных точкой. 
Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.
Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
# The input to the program is a text string containing 4 non-negative integers separated by a dot.
# Write a program that determines whether the entered string of text is a valid IP address.
# Note. The IP address is correct if all 4 numbers are in the range from 0 to 255 inclusive.

n = input().split('.')
n1 = 0
for i in range(len(n)):
    n[i]=int(n[i])
    if 0<=n[i]<=255:
        n1+=1
    else:
        print('НЕТ')
        break
if n1==4:
    print('ДА')
  
  
Sample Input 1:
192.168.0.3
Sample Output 1:
ДА

Sample Input 2:
192.168.0.300
Sample Output 2:
НЕТ

# Interesting number
# Let's call a number interesting if the difference between the maximum and minimum digits is equal to the average digit. 
# Write a program that determines whether a number is interesting or not. If the number is interesting, you should output “Number interesting”, otherwise - “Number uninteresting”.

# Интересное число
# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. 
# Напишите программу, которая определяет, интересное число или нет. Если число интересное, следует вывести «Число интересное», иначе - «Число неинтересное».

a = int(input())   #интересное число если мах - мин = средней цифре
b = a % 10 #единицы
c = (a %100)//10 # десятки
d = a //100 #сотни
x = max(b, c, d)
n = min(b, c, d)
s = (b+c+d)-x-n
if x-n == s:
    print('Число интересное')
elif x-n != s:
    print('Число неинтересное')
  

Sample Input 1:
945
Sample Output 1:
Число интересное
Sample Input 2:
123
Sample Output 2:
Число интересное
Sample Input 3:
896
Sample Output 3:
Число неинтересное

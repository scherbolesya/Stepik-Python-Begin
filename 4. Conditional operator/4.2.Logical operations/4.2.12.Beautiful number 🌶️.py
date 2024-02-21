# Beautiful number 🌶️
# Let's call a number beautiful if it is four-digit and divisible by 7 or 17. 
# Write a program to determine whether the entered number is beautiful. 
# The program should output "YES" if the number is beautiful, or "NO" otherwise.

# Красивое число 🌶️
# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. 
# Напишите программу, определяющую, является ли введённое число красивым. 
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

x = int(input()) 
if 1000<=x<=9999 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')
  
# Sample Input 1:
# 1043
# Sample Output 1:
# YES
# Sample Input 2:
# 1045
# Sample Output 2:
# NO
# Sample Input 3:
# 2751
# Sample Output 3:
# YES

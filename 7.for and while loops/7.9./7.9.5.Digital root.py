# Digital root
# The program input is a natural number n. Write a program that finds the digital root of a given number.
# The digital root of the number n is obtained as follows: if you add up all the digits of this number, then all the digits of the found sum and
# repeat this process until the result is a single-digit number (digit), which is called the digital root of the original number.
# Note. Use nested while loops.
Цифровой корень
На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа. 
Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и 
повторять этот процесс до тех пор, пока в результате не будет получено однозначное число (цифра), которое и называется цифровым корнем изначального числа.
Примечание. Используйте вложенные циклы while.

  
n = int(input())
s = str(n)
while len(s)>1:
    n = 0
    for i in s:
        n+=int(i)
    s=str(n)
print(s)

  
  
Sample Input:
192
Sample Output:
3

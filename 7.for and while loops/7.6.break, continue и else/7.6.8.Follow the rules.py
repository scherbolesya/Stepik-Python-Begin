# Follow the rules
# The program input is a natural number n. Write a program that prints numbers from 1 to n inclusive except:
# - numbers from 5 to 9 inclusive;
# - numbers from 17 to 37 inclusive;
# - numbers from 78 to 87 inclusive.
# Note. Use the continue statement.
Следуй правилам
На вход программе подается натуральное число n. Напишите программу, которая выводит числа от 1 до n включительно за исключением:
- чисел от 5 до 9 включительно;
- чисел от 17 до 37 включительно;
- чисел от 78 до 87 включительно.
Примечание. Используйте оператор continue .


num = int(input())
for i in range(1,num+1):
    if i < 5 or 9<i<17 or 37<i<78 or 87<i:
        print(i)
  
  
Sample Input 1:
10
Sample Output 1:
1
2
3
4
10
Sample Input 2:
20
Sample Output 2:
1
2
3
4
10
11
12
13
14
15
16
Sample Input 3:
1
Sample Output 3:
1

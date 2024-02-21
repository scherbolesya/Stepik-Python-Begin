# YES or NO that is the question
# Write a program that takes a number as input and, depending on the conditions, displays the text “YES” or “NO”.
# Conditions:
# if the number is odd, then output “YES”;
# if the number is even in the range from 2 to 5 (inclusive), then print “NO”;
# if the number is even in the range from 6 to 20 (inclusive), then print “YES”;
# if the number is even and greater than 20, then print “NO”.

# YES or NO вот в чем вопрос
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# Условия:
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

a = int(input())
if a%2 != 0:
    print('YES')
elif a%2==0 and 2<=a<=5:
    print('NO')
elif a%2==0 and 6<=a<=20:
    print('YES')
elif a%2==0 and a>20:
    print('NO')
  

Sample Input 1:
1
Sample Output 1:
YES
Sample Input 2:
2
Sample Output 2:
NO

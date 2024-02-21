# Girls only
# The football team recruits girls from 10 to 15 years old inclusive. Write a program that queries the age and gender of an applicant using 
# the gender symbols m (for male) and f (for female) and determines whether the applicant is eligible to join the team or not. 
# If the applicant is suitable, then print “YES”, otherwise print “NO”.

# Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол претендента, 
# используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. 
# Если претендент подходит, то выведите «YES», иначе выведите «NO».

b = int(input()) #подходит по возрасту
c = input()
if c == "f" and 10 <= b <=15:
    print('YES')
else:
    print("NO")

Sample Input 1:
10
f
Sample Output 1:
YES
Sample Input 2:
11
m
Sample Output 2:
NO

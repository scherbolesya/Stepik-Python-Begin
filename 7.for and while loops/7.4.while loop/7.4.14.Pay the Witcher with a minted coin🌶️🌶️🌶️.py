#  Pay the Witcher with a minted coin🌶️🌶️🌶️
Ведьмаку заплатите чеканной монетой🌶️🌶️🌶️
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево. К тому же ведьмак не принимает купюры, 
он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1,5,10,25.
Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.
# Everyone knows that a witcher is capable of defeating any monster, but his services will not come cheap. 
# In addition, the witcher does not accept banknotes,
# it only accepts minted coins. In the world of the Witcher, there are coins with denominations of 1,5,10,25.
# Write a program that determines the minimum number of minted coins to be paid to the witcher.


a = int(input())
a25 = 0
a10 = 0
a5 = 0
a1 = 0
while a != 0:
    a25 = a // 25
    a10 = a % 25 //10
    a5 = a % 25 % 10 // 5
    a1 = a % 25 % 10 % 5 // 1
    break
print(a25 + a10 + a5 + a1)


Sample Input 1:
49
Sample Output 1:
7
Sample Input 2:
1
Sample Output 2:
1
Sample Input 3:
5
Sample Output 3:
1

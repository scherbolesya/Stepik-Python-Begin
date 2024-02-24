# Asymptotic approximation
# Асимптотическое приближение


from math import * 
total = 0
n = int(input())
for i in range (1,n+1):
    total=total + (1/i)
s = total - log(n)
print(s)


Sample Input 1:
10
Sample Output 1:
0.6263831609742079
Sample Input 2:
1
Sample Output 2:
1.0
Sample Input 3:
100
Sample Output 3:
0.5822073316515288

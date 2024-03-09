# Caesar Cipher 🌶️
Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. 
Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, 
поэтому ученые из НКР не могут понять, как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.
# Caesar's Legion, created in the 23rd century on the basis of the Roman Empire, does not change ancient traditions and uses the Caesar code.
# This let them down, because this cipher is very simple. However, in the post-apocalypse people do not know all the intricacies of the pre-war world,
# Therefore, scientists from the NKR cannot understand how exactly these messages should be decoded. Write a program to decode this cipher.

n = int(input())
# 1<=n<=25
s = input()
for i in s:
    a = ord(i)-n
    if a < 97:
        print(chr(122-(96-a)), end='')
    elif a >=97:
        print(chr(a), end='')
      

Sample Input 1:
1
bwfusvfupdbftbs
Sample Output 1:
avetruetocaesar
Sample Input 2:
14
fsfftsfufksttskskt
Sample Output 2:
rerrfergrweffewewf

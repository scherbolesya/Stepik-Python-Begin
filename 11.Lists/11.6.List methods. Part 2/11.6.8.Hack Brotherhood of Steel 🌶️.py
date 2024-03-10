# Hack Brotherhood of Steel 🌶️
Взлом Братства Стали 🌶️
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали и любезно соглашается помочь им в решении их проблем. 
Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. 
Известно, что программисты Братства никогда не оставляют комментарии к коду и пишут программы на Python, поэтому удаление всех этих комментариев никак 
не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.
Примечание. Обращайте внимание на лишние пробелы в конце строк. Проверяющая система не пропустит ваше решение с ними.
# The Courier, well-known in the Mojave Wasteland, wandered into Hidden Valley - the secret bunker of the Brotherhood of Steel and kindly agrees to help them solve their problems.
# One of these problems was a strange computer virus that manifested itself in the form of comments to programs on the Brotherhood of Steel terminals.
# It is known that Brotherhood programmers never leave comments on the code and write programs in Python, so deleting all these comments is impossible
# won't harm them. Help the scribe Ibsen remove all comments from the program.
# Note. Pay attention to extra spaces at the end of lines. The checking system will not miss your decision with them.

n = input() 
n = n.strip()
n =int(n[1:])
b = []
e = '#'
for i in range (n):
    a = input()
    for j in range(len(a)):
        if a[j] in e:
            a = a[:a.find('#')]
            break
        j +=1    
    a = a.rstrip()#s = s.strip().split()
    b.append(a)
    i +=1
print(*b, sep="\n")#.rstrip())

  
Sample Input:
#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)

Sample Output:
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)

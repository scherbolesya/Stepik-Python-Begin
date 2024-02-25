Тема урока: ревью кода

1.Ревью кода;
2.Поиск ошибок;
3.Производительность кода.
Аннотация. Урок посвящен проведению ревью кода, поиску ошибок и анализу производительности.

---------------------------------------------------------------------------------------------------------
Ревью кода

Ревью кода – проверка исходного кода программы с целью обнаружения и исправления ошибок и неточностей, 
которые остались незамеченными при начальной разработке. 

В процессе ревью кода могут быть исправлены:
- фактические ошибки;
- производительность кода;
- читабельность кода и ошибки форматирования кода.

Целью ревью кода является улучшение качества программного кода и совершенствование навыков программиста.
Как правило ревью кода выполняет программист с большим опытом.

----------------------------------------------------------------------------------------------------------
Фактические ошибки

К фактическим ошибкам в коде относятся ошибки из-за которых код может работать неверно. По сути, это ошибки относящиеся к алгоритму, 
который используется в программе для решения задачи.

Среди частых фактических ошибок встречаются:
- отсутствие начальной инициализации переменной;
- неправильная начальная инициализация переменной;
- отсутствие отступа (в Python блоки кода выделяются отступами);
- неправильные числовые граничные значения, например при использовании функции range();
- неправильные граничные сравнения (путаница с >, >= или <, <=);
- путаница логических операций or и and и т.д.

----------------------------------------------------------------------------------------------------------
Производительность кода

Под производительностью кода в простейшем случае можно подразумевать то, сколько времени программа тратит на решение задачи. 
При написании программы, программист должен думать над тем, сколько времени в худшем случае потребуется его программе для решения задачи.
Рассмотрим задачу, которая проверяет число на простоту.

1 версия программы: Перебираем все числа от 2 до num - 1 и делаем проверку делимости числа num на i:

num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

Если программе на вход подается простое число num = 1934234249, то она будет работать примерно 270 секунд = 4.5 минуты.🙄

2 версия программы: Несложно понять, что перебирать все числа от 2 до num - 1 не имеет смысла. Достаточно проверить числа от 2 до num // 2 + 1:

num = int(input())
flag = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

Если программе на вход подается простое число num = 1934234249, то она будет работать примерно 130 секунд = 2.2 минуты. 
По сути мы улучшили время работы программы вдвое! 😊

3 версия программы: Правую границу num // 2 + 1 проверки можно улучшить, если заметить, что у любого составного числа есть делитель (отличный от 1), 
не превосходящий квадратного корня из числа. Таким образом, имеет смысл перебирать делители от 2 до num+1.

num = int(input())
flag = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

Если программе на вход подается простое число num = 1934234249, то она будет работать примерно 0.066 секунд. 
По сути мы улучшили время работы программы в 4000 раз! 😎

4 версия программы: Предыдущие оптимизации касались случая, когда проверяемое число является простым. 
В случае если число является составным и мы нашли его первый делитель (отличный от 1), мы прерываем цикл с помощью оператора break:

num = int(input())
flag = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

--------------------------------------------------------------------------------------------------------------------
Читабельность кода

Следует помнить, что наш код должен легко читаться другими программистами. Чтобы этого достичь, следует придерживаться стандарта PEP 8. 
Обращайте внимание на следующие моменты:
1.отступы и пробелы: используйте 4 пробела на один уровень отступа и никогда не смешивайте символы табуляции и пробелы;
2.названия переменных: используйте говорящие названия для переменных (total, counter, product) и следуйте стилю lower_case_with_underscores (слова из маленьких букв с подчеркиваниями);
3.пустые строки: дополнительные отступы пустыми строками могут быть изредка полезны для выделения группы логически связанных частей программы: инициализация переменных, основной алгоритм, завершающая проверка и т.д.;
4.комментарии: комментарии должны являться законченными предложениями. И помните, комментарии, которые противоречат коду, хуже, чем отсутствие комментариев. Всегда исправляйте комментарии, если меняете код!
О стандарте PEP 8 на русском языке можно почитать тут.

--------------------------------------------------------------------------------------------------------------------
Примечания

Примечание 1. Хорошие статьи о ревью кода можно почитать на хабре: статья 1, статья 2.
Примечание 2. Программные ошибки, часто называют багами 🦟
Примечание 3. Все программисты создают баги, особенно в начале своего карьерного пути. Это норма 😀

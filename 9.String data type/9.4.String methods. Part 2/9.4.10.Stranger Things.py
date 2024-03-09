Очень странные дела
# Stranger Things
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n различных последовательностей кода Морзе. 
Декодировав их, он получает последовательности из цифр и букв строчного латинского алфавита. 
При этом только в сообщениях Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
Примечание. В сообщениях Оди числа 11 необязательно должны быть разделены другими символами, нужно подсчитать вхождения последовательности символов "11", 
т.е. например в строке "111" содержится одна такая последовательность, в то время как в "1111" их уже две.
# Jim Hopper uses the radio to try to get Odie's message. The receiver receives n different Morse code sequences.
# Having decoded them, he receives sequences of numbers and letters of the lowercase Latin alphabet.
# Moreover, only Odie’s messages contain the number 11, at least 3 times. Help Jim determine the number of messages from Odie.
# Note. In Odi's messages, the numbers 11 do not need to be separated by other characters, but the occurrences of the character sequence "11" must be counted,
# those. for example, the line “111” contains one such sequence, while “1111” already has two.

n = int(input())
counter = 0
for i in range (0,n):

    a = input()
    b = a.count('11')
    if b >= 3:
        counter+=1
print(counter)


Sample Input:
3
11helpme11jim11
avengers141414atta11ck
k1lg0re11111l
Sample Output:
1

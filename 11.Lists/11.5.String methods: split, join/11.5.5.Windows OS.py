Windows OS
В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  
затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу, которая разбирает строку на части, 
разделенные символом "\". Каждую часть вывести в отдельной строке.
Примечание. В Python символ \ обычно используется для создания специальных символьных последовательностей, которые представляют собой управляющие символы 
или экранированные последовательности. Например, \n представляет символ новой строки, \t представляет символ табуляции и т.д. Однако если символ \ используется 
как часть строки, его следует экранировать, т.е. использовать два обратных слэша \\.
# In the Windows operating system, the full file name consists of the drive letter followed by a colon and the "\" character.
# then, using the same symbol, the subdirectories (folders) in which the file is located are listed, at the end the file name is written (C:\Windows\System32\calc.exe).
# The program's input is one line with the correct file name in the Windows operating system. Write a program that parses a string into parts,
# separated by the "\" character. Print each part on a separate line.
# Note. In Python, the \ character is commonly used to create special character sequences that represent control characters
# or escape sequences. For example, \n represents a newline character, \t represents a tab character, etc. However, if the \ character is used
# as part of a string, it should be escaped, i.e. use two backslashes \\.

print(*input().split('\\'), sep="\n")


Sample Input:
C:\Windows\System32\calc.exe

Sample Output:
C:
Windows
System32
calc.exe

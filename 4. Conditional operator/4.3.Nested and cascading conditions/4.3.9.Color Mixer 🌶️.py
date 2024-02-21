# Color Mixer 🌶️
# Red, blue and yellow are called primary colors because they cannot be created by mixing other colors. 
# When two primary colors are mixed, a secondary color is obtained:

# if you mix red and blue, you get purple;
# if you mix red and yellow, you get orange;
# If you mix blue and yellow, you get green.
# Write a program that reads the names of two primary colors to mix. 
# If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. 
# Otherwise, the program should print the name of the secondary color that will be the result.

# Цветовой микшер 🌶️
# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. 
# При смешивании двух основных цветов получается вторичный цвет:

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. 
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», 
# то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, 
# который получится в результате.

a =str(input())  #смешивание цветов
b =str(input())
if a == 'красный' and b == 'желтый' or a == 'желтый' and b =='красный':
    print('оранжевый')
elif a=='синий' and b =='красный' or a =='красный' and b =='синий':
    print('фиолетовый')
elif a =='синий' and b =='желтый' or a =='желтый' and b =='синий':
    print('зеленый')
elif a == 'красный' and b == 'красный':
    print('красный')
elif a =='желтый' and b =='желтый':
    print('желтый')
elif a =='синий' and b =='синий':
    print('синий')
else:
    print('ошибка цвета')


# Sample Input 1:
# красный
# синий
# Sample Output 1:
# фиолетовый
# Sample Input 2:
# красный
# блаблабла
# Sample Output 2:
# ошибка цвета

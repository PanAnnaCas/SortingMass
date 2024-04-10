from PanarinaSortingProject import mass                                                     #
                                                                                            #
mas, n = mass()                                                                             #
print ("\n \n Импорт данных прошел успешно. Ваш массив для сортировки выведен ниже \n" )    #
i=0                                                                                         #
while i<n:                                                                                  #
    print (mas[i], "\n")                                                                    #
    i=i+1                                                                                   #
y = 0
while y<1 or y>5:                                                                           #
    print ("Как мы будем сортировать массив? \n")                                           #
    print ("1 - Быстрая сортировка \n")                                                     #
    print ("2 - Встроенная сортировка \n")                                                  #
    print ("3 - Вставкой \n")                                                               #
    y = int(input ())                                                                       #
mas1 = sorted(mas)
i=0                                                                                         #
while i<n:                                                                                  #
    print (mas1[i], "\n")                                                                    #
    i=i+1                                                                                   #
i=0                                                                                            #

while i<n:                                                                                  #
    mas[i] = sorted(mas[i]) 
    i=i+1                                                                                   #
mas = sorted(mas)
i=0                                                                                         #
while i<n:                                                                                  #
    print (mas[i], "\n")                                                                    #
    i=i+1                                                                                   #
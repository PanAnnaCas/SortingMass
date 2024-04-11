from PanarinaSortingProject import mass                                                     #Ссылаемся на файл со вводом массива
from IntegratedSorting import sortinginteg                                                  #Ссылаемся на файл со встроенной сортировкой                                          #
mas, n = mass()                                                                             #Вводим массив
print ("\n \n Импорт данных прошел успешно. Ваш массив для сортировки выведен ниже \n" )    #
for mas2 in mas:                                                                           #Выводим на экран массив для сортировки
    print (*mas2)                                                                          #                                                                                #
y=10
print ("Как мы будем сортировать массив? \n")                                           
while y:                                                                                   #Выбираем способ сортировки
    if y==0: break
    elif y==1: 
        print ("You've chosen quiksort")
        break
    elif y==2: 
        mas = sortinginteg(mas, n)
        break
    elif y==3: 
        print ("You've chosen вставку")
        break
    else:     
        print ("Выберите один из вариантов: \n")                                           
        print ("1 - Быстрая сортировка \n")                                                     
        print ("2 - Встроенная сортировка \n")                                                  
        print ("3 - Вставкой \n") 
        print ("0 - Выйти из программы \n")
        y = int(input ())
print ("\n Отсортированный массив: \n")
for mas1 in mas:                                                                         #Вывод отсортированного массива
    for mas[i] in mas1:    
        print (f'{mas[i]:4}', end = "|")
    print ("\n")

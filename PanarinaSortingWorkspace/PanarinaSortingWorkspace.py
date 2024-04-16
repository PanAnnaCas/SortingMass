from PanarinaSortingProject import mass                                                     #Ссылаемся на файл со вводом массива
from IntegratedSorting import sortinginteg                                                  #Ссылаемся на файл со встроенной сортировкой                                          #
from QwickSort import qwicksort                                                             #ссылаемся на файл с быстрой сортировкой
from InsertionSort import insertion
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
        mass, t1 = qwicksort (mas, n)
        break
    elif y==2: 
        mass, t2 = sortinginteg(mas, n)
        break
    elif y==3: 
        print ("You've chosen вставку")
        mass, t3 = insertion(mas, n)
        break
    else:     
        print ("Выберите один из вариантов: \n")                                           
        print ("1 - Быстрая сортировка \n")                                                     
        print ("2 - Встроенная сортировка \n")                                                  
        print ("3 - Вставкой \n") 
        print ("0 - Выйти из программы \n")
        y = int(input ())
print ("\n Отсортированный массив: \n")
for mas2 in mass:                                                                         #Вывод отсортированного массива
    for mas0 in mas1:    
        print (f'{mas0:4}', end = "|")
    print ("\n")

print ("\n Время выполнения: ", t1+t2+t3)
print ("\n Время выполнения быстрой сортировки: ", t1)
print ("\n Время выполнения встроенной сортировки: ", t2)
print ("\n Время выполнения сортировки вставкой: ", t3)
def sortinginteg(mas, n):    
    import time
    time1 = time.time()
    mas1 = []                                              #
    for i in mas:                                          #
        mas1 = [*mas1, *i]                                 #"выравниваем" двумерный массив                                                                                                                                                                                     #
    mas1 = sorted(mas1)                                    #Сортируем втроенной функцией одномерный массив
    i=0                                                    #
    for i in range (n):                                    #Делим одномерный массив на срочки двумерного
        mas[i] = mas1[i*n:i*n+n: 1]                        #
 #   for mas2 in mas:                                       #Выводим двумерный массив
 #       print (mas2)                                       #
 
    time2 = time.time()
    t = time2 - time1
    return mas, t
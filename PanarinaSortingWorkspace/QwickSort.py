def qwicksorting (mas):
    import random                                          
    if len(mas)<2:
        return mas
    else:
        reper = random.choice(mas)                       
        small = []                                        
        medium =[]                                        
        larger = []
        for a in mas:                                    
            if a<reper:
                if small != []:
                    small = [a, *small]
                else: small = [a]
            elif a>reper:
                if larger != []:
                    larger = [a, *larger]
                else: larger = [a]
            else:                                        
                medium = [*medium, a]
        return qwicksorting (small) + medium + qwicksorting (larger)

def qwicksort (mas, n):
    import time
    time1 = time.time()                                    #Засекаем время
    mas1 = []                                              #"выравниваем" двумерный массив
    for i in mas:                                          #"выравниваем" двумерный массив
        mas1 = [*mas1, *i]                                 #"выравниваем" двумерный массив                                                                                                                                                                                     #
    mas1 = qwicksorting(mas1)                              #Алгоритм сортировки
    i=0                                                    #Делим одномерный массив на срочки двумерного
    for i in range (n):                                    #Делим одномерный массив на срочки двумерного
        mas[i] = mas1[i*n:i*n+n: 1]                        #Делим одномерный массив на срочки двумерного
    time2 = time.time()                                    #Считаем время работы
    t = time2 - time1                                      #Считаем время работы
    return mas, t

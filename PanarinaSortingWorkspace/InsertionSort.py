def insertion (mas, n):
    import time
    time1 = time.time()
    mas1 = []                                              #"выравниваем" двумерный массив
    for i in mas:                                          #"выравниваем" двумерный массив
        mas1 = [*mas1, *i]                                 #"выравниваем" двумерный массив
    for i in range(1, n*n):
        j=i
        a=mas1[i]
        while j>0 and mas1[j-1]>a:
            mas1[j] = mas1[j-1]
            j=j-1
        mas1[j]=a    
    i=0                                                    #Делим одномерный массив на срочки двумерного
    for i in range (n):                                    #Делим одномерный массив на срочки двумерного
        mas[i] = mas1[i*n:i*n+n: 1]                        #Делим одномерный массив на срочки двумерного
    time2 = time.time()
    t = time2 - time1
    return mas, t

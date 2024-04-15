def qwicksort (mas, n):
    import time
    import random                                          #Засекаем время
    time1 = time.time()
    mas1 = []                                              #
    for i in mas:                                          #
        mas1 = [*mas1, *i]                                 #"выравниваем" двумерный массив                                                                                                                                                                                     #
    
    if len(mas1)<2:
        return mas, 0.0
    else:                                                 #обработка массива
       
        while len(mas1)>0:   
            reper = random.choice(mas1)                       
            small = []                                        
            medium =[]                                        
            larger = []
            for a in mas1:                                    
                if a<reper:
                    if small != []:
                        if a<random.choice(small):
                            small = [a, *small]
                        else: small = [*small, a]
                    else: small = [a]
                elif a>reper:
                    if larger != []:
                        if a<random.choice(larger):
                            larger = [a, *larger]
                        else: larger = [*larger, a]
                    else: larger = [a]
                else:                                        
                    medium = [*medium, a]
                   
            #if random.choice(mas)<random.choice(medium): mas=[*mas, medium]
            #else:mas=[medium, *mas]
            mas1=[]
            mas2 = [*small, *medium, *larger]                 

        mas1=mas2
        i=0                                                    #
        for i in range (n):                                    #Делим одномерный массив на срочки двумерного
            mas[i] = mas1[i*n:i*n+n: 1]                        #
        
        time2 = time.time()
        t = time2 - time1
        return mas, t

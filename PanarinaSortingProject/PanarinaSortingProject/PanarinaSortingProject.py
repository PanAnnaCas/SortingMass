def mass():    
    m = int(input("How much elements in a row do you want?\n"))                           #Инициализация массива
    print ("Do you want it to be random \n Yes or No")                                    #Инициализация массива
    ans = "";                                                                             #Инициализация массива
    n= [[0 for j in range(m)] for i in range(m)]                                          #Выбираем способ заполнения массива
    while ans != "Yes" and ans != "No":                                                   #Выбираем способ заполнения массива
        ans = input()                                                                     #Выбираем способ заполнения массива
        if ans == "Yes":                                                                  #Выбираем способ заполнения массива
             for i in range(m):                                                           #Выбираем способ заполнения массива
                 for g in range(m):                                                       #Выбираем способ заполнения массива
                    import random                                                         #Выбираем способ заполнения массива
                    n[i][g] = random.randint (-1000, 1000)                                #Выбираем способ заполнения массива
        elif ans == "No":                                                                 #Выбираем способ заполнения массива
            print ("Insert elements one by one")
            for i in range(m):                                                            #Выбираем способ заполнения массива
                for g in range(m):                                                        #Выбираем способ заполнения массива
                    n[i][g] = int(input ())                                               #Выбираем способ заполнения массива
        else: print ("Try again")                                                         #Выбираем способ заполнения массива
        print (ans, "\n")                                                                 #Выбираем способ заполнения массива
#   for i in range(m):                                                                    #Просто вывод какой-то
#       for g in range(m):                                                                #Просто вывод какой-то
#            print (n[i][g], " is ", i, ", ", g, " out of ", m, "\n")                     #Просто вывод какой-то
                                                                                          #Просто вывод какой-то
    for i in range(m):                                                                    #Просто вывод какой-то
        print (*n[i])                                                                     #Просто вывод какой-то
    return n, m

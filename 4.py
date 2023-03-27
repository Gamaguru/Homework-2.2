text = input("Пожалуйста, введите свой текст : ")
T = text.split()
for x, y in enumerate (T, start=1) :
    if len(y) > 11 :
        y = y[:10]
        print(x, y)
    else :
        print (x,y)
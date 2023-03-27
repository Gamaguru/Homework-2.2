rate_list = [7, 5, 3, 3, 2]
frq = int(input("Сколько ставок вы хотите добавить?\n\t ВВЕДИТЕ КОЛИЧЕСТВО: "))
for j in range(frq):
    add_new = int(input("Какую оценку вы хотите добавить?\n\t ВВЕДИТЕ СКОРОСТЬ: "))
    if add_new in rate_list:
        i = rate_list.index(add_new)
        while (i + 1) <= (len(rate_list) - 1) and (rate_list[i] == rate_list[i + 1]):
            i += 1
        rate_list.insert(i, add_new)
        print(f"rate_list {rate_list}")
    else:
        if add_new <= rate_list[-1]:
            rate_list.append(add_new)
            print(f"rate_list {rate_list}")
        else:
            rate_list.insert(0, add_new)
            print(f"rate_list {rate_list}")
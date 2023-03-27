q = int(input("Сколько элементов в список вы хотите добавить?\n\t Введите количество элементов: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Предмет # {i + 1} : "))
print(f"Просмотр списка ваших товаров:\n{my_lst}")
for x in range(0, (len(my_lst) - 1),2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Ваш ИЗМЕНЕННЫЙ вид списка элементов:\n{my_lst}")
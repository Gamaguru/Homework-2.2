month = int(input("Пожалуйста, введите идентификатор месяца от 1 до 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tНЕВЕРНЫЙ ИДЕНТИФИКАТОР!!! \n\tпожалуйста, используйте только диапазон чисел от 1 до 12!")
        month = int(input("Пожалуйста, введите идентификатор месяца от 1 до 12 : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tСезон, связанный с вашим идентификатором месяца#{month}  это '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tСезон, связанный с вашим идентификатором месяца# {month} это '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tСезон, связанный с вашим идентификатором месяца# {month} это '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tСезон, связанный с вашим идентификатором месяца# {month} это '{mlist[3]}'")
        break
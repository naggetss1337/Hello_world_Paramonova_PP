pH = float(input("Введите ph среды:"))
if pH < 7:
    print("Кислая среда")
elif pH > 7:
    print("Щелочная среда")
elif pH == 7:
    print("Нейтральная среда")
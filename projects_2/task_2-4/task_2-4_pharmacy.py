capsules = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input("Введите вместимость одной упаковки: "))
full_capsules = capsules//capacity
remains = capsules%capacity
print("Отчет фасовочного цеха\t ˎˊ˗\n")
print(f"Полных упаковок:\t{full_capsules}\n")
print(f"Остаток капсул:\t{remains}\n") 
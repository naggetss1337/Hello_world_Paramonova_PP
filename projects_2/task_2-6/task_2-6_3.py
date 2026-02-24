phenotype_donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_recipient = input("Введите фенотип группы крови пациента(реципиента) (I, II, III, IV): ").strip().upper()

control = ["I", "II", "III", "IV"]
if phenotype_donor not in control or phenotype_recipient not in control:
    print("Введена несуществующая группа крови")
elif phenotype_donor == phenotype_recipient or phenotype_donor == "I":
    print("Переливание возможно")
else:
    print("Переливание невозможно")
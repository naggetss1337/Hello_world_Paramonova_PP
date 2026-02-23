donor_phenotype = input("Введите донорский фенотип группы крови(I, II, III, IV): ").strip().upper()
patient_phenotype = input ("Введите пациенский фенотип группи крови (I, II, III, IV): ").strip().upper()
if patient_phenotype == "I" and donor_phenotype == "I":
    print("Переливание возможно")
else:
    print("Переливание невозможно")
if patient_phenotype == "II" and donor_phenotype == "I" or donor_phenotype == "II":
    print("Переливание возможно")
else:
    print("Переливание невозможно")
if patient_phenotype =="III" and donor_phenotype == "I" or donor_phenotype == "III":
    print("Переливание возможно")
else:
    print("Переливание невозможно")
if patient_phenotype == "IV" and donor_phenotype == "I" or donor_phenotype == "II" or donor_phenotype == "III" or donor_phenotype == "IV":
    print("Переливание возможно")
else:
    print("Неккоретно введенные данные")


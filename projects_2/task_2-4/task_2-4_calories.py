protein_num = input("Количество белков в продукте(г):")
protein = int(protein_num)
lipids_num = input("Количество жиров в продукте:")
lipids = int(lipids_num)
carbohydrates_num = input("Введите количество углеводов в продукте:")
carbohydrates = int(carbohydrates_num)
ccal = (protein*4)+(lipids*9)+carbohydrates*4
print(f"Итоговая калорийность: {ccal}")
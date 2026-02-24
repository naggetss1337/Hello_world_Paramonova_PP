dna = input("Введите последовательность днк: ").upper()
count_A = dna.count("A")
count_T = dna.count("T")
count_C = dna.count("C")
count_G = dna.count("G")
count_all = len(dna)
# Подсчет процентного содержания каждого из нуклеотидов
procent_A = (count_A/count_all)*100
procent_T= (count_T/count_all)*100
procent_C = (count_C/count_all)*100
procent_G = (count_G/count_all)*100
print("Анализ последовательности днк\t/ᐠ > ˕ <マ\n")
print(f"Последовательность днк в верхнем регистре:\t{dna}\n")
print(f"Подсчет нуклеотидов:\nA:\t{count_A}\nT:\t{count_T}\nC:\t{count_C}\nG:\t{count_G}\n")
print(f"Общая длина цепи днк:\t{count_all}\n")
print(f"Процентное содержание каждого нуклеотида в цепи:\n")
print(f"A:\t{procent_A}\nT:\t{procent_T}\nC:\t{procent_C}\nG:\t{procent_G}\n")
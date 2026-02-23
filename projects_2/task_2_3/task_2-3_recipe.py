nutrient_medium = input("Какая питательная среда будет необходима?")
agar_concentration = input("Какая концентрация агара будет необходима(%)?")
sterilization_temperature = input ("Какая температура стерилизации будет необходима?")
with open ("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"\t{nutrient_medium}\n Концентрация агара:\t{agar_concentration}\n Температура стерилизации:\t{sterilization_temperature}")
print("Файл 'recipe.txt' был успешно сформирован!")  
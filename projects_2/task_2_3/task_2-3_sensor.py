name_operator = input("Введите имя оператора:")
sensor_value = input("Введите значение датчика давления (Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
    sensor.write(f"ОПЕРАТОР:{name_operator}\tЗНАЧЕНИЕ:{sensor_value}")
print("Данные успешно сохранены в sensor_log.txt")
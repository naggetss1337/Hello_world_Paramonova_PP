exploer_name = input("Введите ФИО исследователя:")
data = input("Введите дату исследования:")
experiment = input("Введите название эксперимента:")
conclusion = input("Введите сделанный из исследования вывод:")
with open ("journal.txt", "w", encoding="utf-8") as journal:
    journal.write(f"─━─━─━─━─━─━─━─━─━─━─━─━─━\n╷\tЭлектронный лабороторный журнал\t╷\n─━─━─━─━─━─━─━─━─━─━─━─━─━\n")
    journal.write(f"╷\tФио исследователя:{exploer_name}\t╷\n")
    journal.write(f"╷\tДата:{data}\t╷\n")
    journal.write(f"╷\tЭксперимент:{experiment}\t╷\n")
    journal.write(f"─━─━─━─━─━─━─━─━─━─━─━─━─━\n╷")
    journal.write(f"╷\tВывод:{conclusion}\t╷\n")
    journal.write(f"─━─━─━─━─━─━─━─━─━─━─━─━─━\n")




    
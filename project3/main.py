msg = "     /remind 90 купить хлеб  "
msg = msg.strip().lower()
msg = msg.split()
rememberspis = []
if msg[0].startswith("/"):
    for i in msg:
        if i.isdigit() == True:
            time = i
        else:
            remember = i
            rememberspis.append(remember)
    rememberspis.pop(0)
    remember = " ".join(rememberspis)
    print(f"Напомнить через {time} мин: {remember}")
else:
    print("Это не команда.")


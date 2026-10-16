text = input("Введите Ваш текст:")
correct = text.strip(" ")
if correct == "":
    print("Пустое сообщение")
else:
    correct = correct[0].upper() + correct[1:]
    if correct.endswith((".", "!", "?")):
        print(correct)
        print(f"Символов было: {len(text)}, стало: {len(correct)}")
    else:
        correct = correct + "."
        print(correct)
        print(f"Символов было: {len(text)}, стало: {len(correct)}")
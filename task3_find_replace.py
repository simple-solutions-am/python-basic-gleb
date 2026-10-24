s = "Python - лучший язык. Учу Python каждый день!"
print("Python" in s, "python" in s)
print(s.find("Python"), s.find("Python", 1))
print(s.find("Java"))
print(s.count("Python"))
print(s.replace("Python", "Питон"))

a = "Клуб"
b = "клуб"
print(a == b, a.lower() == b.lower(), a.upper() == b.upper())

phrase = "А роза упала на лапу Азора"
print(phrase.lower().replace(" ", ""))
print(phrase.lower().replace(" ", "") == phrase.lower().replace(" ", "")[::-1])
phrase = "Привет мир"
print(phrase.lower().replace(" ", "") == phrase.lower().replace(" ", "")[::-1])

text = "Кто идет на мит? Я иду! Глеб, ты идешь на мит? Мит в субботу, не опаздывай, Глеб!"
text = text.lower()
for i in ".,!?":
    text = text.replace(i, "")
counts = {}
max_count = 0
text2 = text.split()
for w in text2: 
    counts[w] = counts.get(w, 0) + 1
    if counts.get(w) > max_count:
        max_count = counts.get(w)
        name_max_count = w

for i, x in counts.items():
    print(f"{i}:{x}")

print(f"Больше всего: {name_max_count}:{max_count}")
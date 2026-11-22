
anya = {"игры", "футбол", "боты", "аниме"}
lev = {"аниме", "музыка", "игры", "шахматы"}
kira = {"футбол", "код", "боты"}



general = []

for i in anya:
    for x in lev:
        if i == x:
            general.append(i)
print(f"Общее у Ани и Льва: {sorted(general)}")

all = list({x for s in (anya, lev, kira) for x in s})
all = sorted(all)
print(all)

unique_lev = []

for i in lev:
    unique_lev.append(i)

for i in anya:
    for x in unique_lev:
        if i == x:
            unique_lev.remove(i)
for i in kira:
    for x in unique_lev:
        if i == x:
            unique_lev.remove(i)

print(sorted(unique_lev))
print(bool(lev & kira), bool(anya & kira))

tags = ["python", "бот", "игры", "python", "aiogram", "бот", "python"]
print((len(tags)), (len(set(tags))))
print(sorted(set(tags)))
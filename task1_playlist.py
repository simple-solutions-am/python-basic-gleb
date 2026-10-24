
playlist = []
playlist.append('Утро')
playlist.append('Дорога')
playlist.append('Тренировка')

print(len(playlist))
print(playlist[0], playlist[-1])
print(playlist[:2])
print("Дорога" in playlist)

playlist[1] = "Дорога домой"
playlist.insert(0, "Интро")
playlist.insert(4, "Финал")
skipped = playlist[-1]
playlist.pop(-1)
playlist.remove("Утро")
print(f"{playlist} | Пропустили: {skipped}")

for i, track in enumerate(playlist, start = 1):
    print(f"{i}. {track}")

tracks = [("Интро", 95), ("Дорога домой", 214), ("Тренировка", 187), ("Финал", 241)]
first = tracks[0]
title = first[0]
seconds = first[1]
print(first, first.__class__)
print(title, seconds)

seconds1 = 0
for x in tracks:
    seconds1 += x[1]
minutes, seconds1 = divmod(seconds1, 60)
print(f"Всего: {minutes:02d}:{seconds1:02d}")

maxtime = 0
for x in tracks:
    if x[1] > maxtime:
        maxtime = x[1]
        trackmax = x[0]
tracks200 = []
for x in tracks:
    if x[1] < 200:
        tracks200.append(x[0])

print(f"Самый длинный: {trackmax}")     
print(f"Короче 200 секунд: {tracks200}")

names = ["Тренировка", "Интро", "Финал", "Дорога домой"]
print(sorted(names))
print(names)
result = names.sort()
print(result)
print(names)
alph = sorted(names, reverse=True)
print(alph[0:2])

queue = playlist
queue.append("Бонус")
print(playlist)
backup = playlist.copy()
backup.append("Еще один")
print(len(playlist), len(backup))
print(queue is playlist, backup is playlist)

lines = [
    "🎧 Плейлист: 4 трека, 12:17",
    "1. Интро - 1:35",
    "2. Дорога домой - 3:34",
    "3. Тренировка - 3:07",
    "4. Финал - 4:01",
]

print("\n".join(lines))


    

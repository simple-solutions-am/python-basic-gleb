time = int(input())
hour = time // 3600
minute = (time % 3600) // 60
sec = time % 60
print(f'{hour:02d}:{minute:02d}:{sec:02d}')
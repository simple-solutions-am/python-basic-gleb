digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 7]
print(digits[0], digits[-1])
print(digits[5], digits[-4])
print(digits[2:6])
print(digits[::2])
print(digits[::-1])
print(digits.count(1), digits.count(5))
print(min(digits), max(digits), sum(digits))
print(digits.index(5))
print(len(digits) - 1 - digits[::-1].index(5))
target = 5
index = []
for i, x in enumerate(digits, start = 0):
    if x == target:
        index.append(i)
print(index)

if 7 in digits:
    print(digits.index(7))
else:
    print("7 не найдено.")


target = 5
digits5 = digits.copy()
for i, x in enumerate(digits, start = 0):
    if x == target:
        index.append(i)
    for y in index:
        digits5.pop(y)
        digits5.insert(y, 0)
print(digits5)
print(digits)

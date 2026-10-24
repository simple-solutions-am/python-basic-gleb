
print(f"{7:03d}, {74:03d}, {743:03d}, {7438:03d}")
print(f"{1499.5:.2f}")
print(f"{1234567.891:,.2f}")
print(f"{1234567.891:,.2f}".replace(",", " "))
print(f"{0.875:.1%}")
day = 5
month = 3
year = 2027
print(f"{day:02d}.{month:02d}.{year:02d}")
print(f"{"Чек":*^20}")

cart = [("Хлеб", 45), ("Молоко", 89), ("Чокопай", 120)]
total = sum(price for name, price in cart)
for i, x in cart:
    print(f"{i:<10}{x:>6}руб.")
print(f"{'Итого':<10}{total:>6} руб.")
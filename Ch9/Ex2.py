приховане_повідомленя = ("це якщо не ти дуже це хороший чітаєш спосіб то заховати щось повідомленя негаразд")
повідомленя = приховане_повідомленя.split(" ")

print("перше повідомленя:")
print(" ")

for x in range(0, 13, 2):
    print(повідомленя[x])
print(" ")
print("друге повідомленя:")
print(" ")

for x in range(1, 14, 2):
    print(повідомленя[x])
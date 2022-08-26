file = open("привет!!!.txt", encoding="utf-8")
file2 = open("привет!!!2.txt", "w", encoding="utf-8")
file2.write(file.read())
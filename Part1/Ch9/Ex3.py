file = open("hi!!!.txt", encoding="utf-8")
file2 = open("hi!!!2.txt", "w", encoding="utf-8")
file2.write(file.read())
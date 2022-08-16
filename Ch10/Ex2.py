import pickle
улюблені_речі = ["кубик-рубик",
                 "яблуко",
                 "телефон",
                 "галубика",
                 "лего", 234, 345, 456, 567]

file = open("save.dat", "wb")
pickle.dump(улюблені_речі, file)
file.close()
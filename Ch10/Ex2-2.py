import pickle

file = open("save.dat", "rb")
result = pickle.load(file)

print(result)
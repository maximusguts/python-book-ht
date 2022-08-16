import time
def багато_чисел(макс):
    t1 = time.time()
    for x in range(0, макс):
        print(x)
    t2 = time.time()
    print("знадобилося %s секунд" % (t2-t1))
    if t2-t1 >= 0.995 and t2-t1 <= 1.005:
        exit()
    else:
        багато_чисел(119000)

багато_чисел(119000)
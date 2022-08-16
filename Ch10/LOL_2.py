import time
def багато_чисел(макс):
    t1 = time.time()
    for x in range(0, макс):
        pass
    t2 = time.time()
    print("знадобилося %s секунд" % (t2-t1))

багато_чисел(1000000000)
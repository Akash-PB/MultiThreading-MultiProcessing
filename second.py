import random
import operator
import time
import threading

start = time.time()


operator = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]


def sequence():
    for i in range(200):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        op, fn = random.choice(operator)
        print("{}{}{}={}".format(a, op, b, fn(a, b)))
        #time.sleep(1)


t1 = threading.Thread(target=sequence, args=())
t2 = threading.Thread(target=sequence, args=())

t1.start()
t2.start()
t1.join()
t2.join()

'''for i in range(5):
    i = threading.Thread(target=sequence, args=())
    i.start()
    i.join()'''


end = time.time()
# print(f"Runtime of the Program is:={end-start}")
print("Runtime of the Program is:= {}".format(end - start))

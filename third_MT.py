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


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=sequence)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


main()

end = time.time()
# print(f"Runtime of the Program is:={end-start}")
print("Runtime of the Program with threading is:= {}".format(end - start))

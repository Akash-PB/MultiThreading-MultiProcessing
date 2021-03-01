import random
import operator
import time
import multiprocessing
from multiprocessing.dummy import freeze_support

start = time.time()

operator = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]


def sequence():
    for i in range(100):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        op, fn = random.choice(operator)
        print("{}{}{}={}".format(a, op, b, fn(a, b)))

        #time.sleep(1)


def main():
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=sequence(), args=())
        jobs.append(p)
        p.start()
        p.join()


if __name__ == "__main__":
    main()

end = time.time()
# print(f"Runtime of the Program is:={end-start}")
print("Runtime of the Program with threading is......:= {}".format(end - start))

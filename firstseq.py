import random
import operator
import time
from threading import *

start = time.time()


class First:
    """def __init__(self, operator):
        self.operator = operator"""

    operator = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]

    for i in range(200):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        op, fn = random.choice(operator)
        print("{}{}{}={}".format(a, op, b, fn(a, b)))
        # time.sleep(1)


end = time.time()
# print(f"Runtime of the Program is:={end-start}")
print("Runtime of the Program is:= {}".format(end - start))

import time
from typing import Callable


def user_input():
    user_in = input("what number do you want to check? ")
    return int(user_in)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Elapsed time: {end - start:.6f} seconds")
        return result
    return wrapper


def even(n):
    return n // 2


def odd(n):
    return 3 * n + 1


@timer
def main(n):
    print(f"n = {n}")
    max_n = n
    counter = 0
    while True:
        if n == 1:
            return f"took {counter} steps to reach 1. Had a maximum value of {max_n}"
        if n > max_n:
            max_n = n
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
        counter += 1


# from openai
def collatz_steps(n, steps_cache={1: 0}):
    if n in steps_cache:
        return steps_cache[n]
    else:
        if n % 2 == 0:
            steps = collatz_steps(n // 2, steps_cache) + 1
        else:
            steps = collatz_steps(n * 3 + 1, steps_cache) + 1
        steps_cache[n] = steps
        return steps


# way slower and has recursive depth limit
def recursive(n, steps=0):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return recursive(n // 2, steps=steps + 1)
    else:
        return recursive(3 * n + 1, steps + 1)


@timer
def att3(n):
    while True:
        print(f"n = {n}")
        max_n = n
        counter = 0
        while True:
            if n == 1:
                return f"took {counter} steps to reach 1. Had a maximum value of {max_n}"
            if n > max_n:
                max_n = n
            if n % 2 == 0:
                n = even(n)
            else:
                n = odd(n)
            counter += 1


class Memo:
    def __init__(self, func: Callable):
        self.func = func
        self.memo_dict = {}

    def access(self, key):
        if key in self.memo_dict:
            return self.memo_dict[key]
        else:
            self.memo_dict[key] = self.func(key)
            return self.memo_dict[key]

    def __getitem__(self, item):
        return self.access(item)



if __name__ == "__main__":
    # print(main(user_input()))
    # check = (random.randint(10*10_000, 10**10_001))
    # check = (random.randint(10*100, 10**101))
    # print(f"check = {check}")
    # print(f"{len(str(check))} digits")

    # s = time.perf_counter()
    # print(main(check))
    # e = time.perf_counter()
    # first = e - s
    # print(f"took {first}")
    #
    # s = time.perf_counter()
    # print(collatz_steps(check))
    # e = time.perf_counter()
    # second = e - s
    # print(f"took {second}s")
    # print(f"second < first? {second < first}")
    m = Memo(att3)
    print(main(1000041))



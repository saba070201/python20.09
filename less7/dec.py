def simple_decorator(func):
    def wrapper():
        print('функция выполняется')
        func()
        print('функция закончила выполнение')

    print(type(wrapper))
    return wrapper


@simple_decorator
def hello_world(a):
    print(a)


# hello_world('lalala')
simple_decorator(hello_world)
import time
from random import randint


def get_time(iters):
    def decorator(func):
        def wrapper(*args, **kwargs):
            d=iters
            sum=0
            while d!=0:
                st = time.time()
                rv = func(*args, **kwargs)
                et = time.time()
                ft = et - st
                sum = sum + ft
                d = d - 1
            time1 = sum /iters
            print(f'time:{time1}')
            return rv


        return wrapper
    return decorator


@get_time(10)
def CombSort(arr: list):
    step = int(len(arr) / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(arr):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                swap += 1

            i += 1
        if step > 1:
            step = int(step / 1.247)
        return True


CombSort([1, 2, 0, 1])
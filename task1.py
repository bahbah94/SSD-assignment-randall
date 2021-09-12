import time,io
import contextlib

def decorator_1(fun):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args,**kwargs)
        end = time.perf_counter()
        s = f.getvalue()
        #print(f"{fun.__name__} executed {end} sec")
        print(f"{fun.__name__} call {wrapper.count} executed in {end} seconds")

    wrapper.count = 0
    return wrapper

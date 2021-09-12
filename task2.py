
import inspect,contextlib,io,time


def decorator_2(fun):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args,**kwargs)
        end = time.perf_counter()
        s = f.getvalue()
        #print(f"{fun.__name__} executed {end} sec")
        print(f"{fun.__name__} call {wrapper.count} executed in {end} seconds")
        print("Name:    ", fun.__name__)
        print("Type:    ",type(fun))
        print("Sign:    ",inspect.signature(fun))
        print("Args:",end="    " )
        print("Positional: ",locals()['args'])
        print("         key-worded:  ",locals()['kwargs'])
        print("Doc:     ",inspect.getdoc(fun))
        print("Source:      ",inspect.getsource(fun))
        print("Output:  ",fun(*args,**kwargs))
    wrapper.count = 0
    return wrapper

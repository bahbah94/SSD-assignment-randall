import logging,time,inspect,contextlib,io



def decorator_4(fun):
    #now we will Create and configure logger
    logging.basicConfig(filename="std.log",
    					format='%(asctime)s %(message)s',
    					filemode='a')

    logger=logging.getLogger()
    def wrapper(*args,**kwargs):
        ###using logger will dump the error into a log file.
        try:
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
        except Exception as e:
            logger.error(e)
    wrapper.count = 0
    return wrapper
